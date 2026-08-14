# 求职自动化 Workflow 连接器

English docs: [README.md](README.md)

这是一个去个人信息的公开版连接器，用来把两个上游 Codex skills 串成一套可复用的求职流程：

- 岗位抓取与关键词提炼：`Shuboya1030/linkedin-keyword-resume-coach`
- 投递管理与辅助提交：`yvonnehe772/applypilot`

这个仓库只保留依赖安装、workflow 连接、空模板和安全规则。它不包含真实简历、申请记录、浏览器会话、cookies、截图或任何候选人的私人资料。

## 它能做什么

1. 安装 workflow 所需的本地依赖。
2. 引导安装两个上游 skills。
3. 初始化岗位池和投递日志 dashboard。
4. 把每日岗位抓取、高频 JD/requirement 提炼、简历路由、cover letter 生成、投递执行串起来。
5. 支持两种投递模式：
   - `海投 / Volume`：使用预先准备好的简历版本，适合低风险、低摩擦岗位。
   - `精投 / Precision`：根据岗位描述调整简历和 cover letter，提交前需要用户确认。

## 它不会做什么

- 不绕过验证码、登录、2FA、反自动化检查、付费墙或平台限制。
- 不编造工作经历、签证/工签身份、薪资、学历、证书或工作成果数据。
- 不重新分发未授权的上游源码。
- 不保证所有招聘网站都能全自动投递。

## 平台支持

最适合先从 LinkedIn Easy Apply 测试，因为流程相对稳定。

SEEK、Glassdoor、Greenhouse、Lever、Workday、公司官网 ATS 等平台可以在浏览器自动化能力允许时扩展。但遇到长表单、验证码、登录切换、敏感法律问题或不确定事实时，应交回用户处理。

## 快速开始

```bash
./scripts/install_dependencies.sh
./scripts/install_upstream_skills.sh
./scripts/init_workspace.sh ./my-private-job-workflow
```

然后在 Codex 里使用：

```text
使用这个 job application workflow connector。先做 onboarding，创建我的私人 candidate profile 和 application rules，然后先跑 lead-finding-only trial，不要直接真实投递。
```

## 文件结构

```text
config/      Workflow 示例配置。
dashboard/   空白 CSV dashboard 模板。
docs/        中英文 workflow、安全和平台说明。
scripts/     依赖安装与私有工作区初始化脚本。
templates/   候选人信息、回答库、简历路由、投递规则模板。
```

## 隐私规则

候选人的真实资料应该放在 `scripts/init_workspace.sh` 创建的私有工作区里，不要提交到 GitHub。

发布前建议运行：

```bash
python3 scripts/check_no_private_data.py .
```

## 许可证

本连接器使用 MIT License 发布。

上游项目保留各自许可证：

- `yvonnehe772/applypilot`：MIT License。复用其材料时需要保留版权和许可声明。
- `Shuboya1030/linkedin-keyword-resume-coach`：准备本连接器时没有看到明确许可证，所以本仓库只提供安装引用和连接说明，不重新分发其源码。

