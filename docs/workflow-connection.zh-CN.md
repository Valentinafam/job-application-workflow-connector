# Workflow 连接说明

这个连接器把岗位发现和投递执行串起来，但不把候选人的私人资料放进公开仓库。

## 流程

1. Onboarding
   - 创建私有 candidate profile。
   - 定义 application rules。
   - 添加简历版本和 resume routing 规则。
   - 确认可复用的 answer bank。

2. 岗位抓取
   - 每天或每两天运行一次岗位抓取 skill。
   - 把岗位写入 `dashboard/job_pool.csv`。
   - 提炼 JD 和 requirements 的高频关键词。
   - 按岗位大类、匹配度、优先级和 blocker 分类。

3. 简历和 Cover Letter 路由
   - 海投模式按岗位大类使用固定简历版本。
   - 精投模式根据具体 JD 修改简历和 cover letter。
   - 除非平台没有上传或输入入口，每个申请都应生成 cover letter。

4. 投递执行
   - 只投符合用户规则的岗位。
   - 遇到验证码、登录、2FA、不清楚的法律事实、敏感问题、上传无法确认时停止。
   - 每次尝试都写入 `dashboard/application_log.csv`。

5. Dashboard 复盘
   - 展示每日统计、岗位池、投递状态、blocker 和 follow-up。
   - 把重复问题沉淀到 `dashboard/automation_rules.csv`。

## 模式规则

海投模式：

- 使用已有简历版本。
- 在用户授权后，对低风险、短流程岗位快速提交。
- 不为普通岗位临时改简历，除非规则把它升级为精投。

精投模式：

- 修改简历和 cover letter。
- 提交前让用户确认材料和最终提交。
- 适合高匹配岗位、政府岗位、复杂表单或战略性雇主。

## 状态流转

```text
Found -> Screened -> Pending
Found -> Screened -> Skipped
Pending -> Applying -> Submitted
Pending -> Applying -> Blocked
Pending -> Needs user -> Applying
```

只有看到明确提交成功证据，才计为 `Submitted`。

