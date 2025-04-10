# AstrBot 60秒新闻插件

![示例图片](https://api.03c3.cn/api/zb?type=img)

基于 [bbpn-cn/headline](https://github.com/bbpn-cn/headline) 项目改进的AstrBot插件，优化了接口稳定性和配置灵活性。

## ✨ 改进亮点

- ✅ **接口稳定性增强**：新增自动验证机制，确保接口可用性
- ⚙️ **可配置化**：支持自定义新闻源API地址
- 🛠️ **错误处理优化**：完善的异常处理和用户提示
- 🔄 **兼容性保留**：完全兼容原项目功能

## 功能特性

- 通过指令 `/今日新闻` 获取最新新闻图片
- 自动验证新闻接口可用性
- 支持自定义新闻源API地址
- 内置默认稳定接口地址
- 友好的错误提示信息

## 安装方法

1. 将插件文件夹 `astrbot_plugin_60s_news` 放入AstrBot的插件目录
2. 重启AstrBot服务

## 配置说明

编辑 `_conf_schema.json` 文件可修改以下配置：

```json
{
    "api_url": {
        "description": "60秒新闻图片API地址（可替换为其他稳定接口）",
        "type": "string",
        "default": "https://api.03c3.cn/api/zb?type=img",
        "examples": [
            "https://api.03c3.cn/api/zb?type=img",
            "http://backup.api/news"
        ]
    }
}
```
