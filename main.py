"""用户输入 /今日新闻 获取60秒读懂世界图片"""
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
import aiohttp
import asyncio

# 移除错误的 config 导入行

@register("astrbot_plugin_60s_news", "egg", "60秒国内新闻", "1.0.0", "https://github.com/bbpn-cn/headline")
class NewsPlugin(Star):
    def __init__(self, context: Context, config: dict = None):
        super().__init__(context)
        # 修改配置获取方式
        self.api_url = config.get("api_url", "https://v.api.aa1.cn/api/60s-v3/") if config else "https://v.api.aa1.cn/api/60s-v3/"

    async def verify_image(self, session):
        """验证接口是否返回图片"""
        try:
            async with session.get(self.api_url) as response:  # 修改为 self.api_url
                if response.status == 200:
                    content_type = response.headers.get('Content-Type', '')
                    if isinstance(content_type, bytes):
                        content_type = content_type.decode('utf-8')
                    if content_type.startswith('image/'):
                        return True
                return False
        except aiohttp.ClientError:
            return False

    @filter.command("今日新闻")
    async def news_command(self, event: AstrMessageEvent):
        '''新闻查询指令，使用格式：/今日新闻'''
        yield event.plain_result("正在获取今日新闻...")

        async with aiohttp.ClientSession() as session:
            if await self.verify_image(session):
                yield event.image_result(self.api_url)  # 修改为 self.api_url
            else:
                yield event.plain_result("无法获取今日新闻，请稍后再试。")

    async def terminate(self):
        '''插件卸载时调用'''
        pass

if __name__ == "__main__":
    # 修复测试代码中的 API_URL 未定义问题
    async def test():
        async with aiohttp.ClientSession() as session:
            test_url = "https://v.api.aa1.cn/api/60s-v3/"  # 添加临时测试URL
            async with session.get(test_url) as response:
                if response.status == 200:
                    data = await response.read()
                    print("图片数据获取成功，长度:", len(data))
                else:
                    print("获取失败，状态码:", response.status)

    asyncio.run(test())
