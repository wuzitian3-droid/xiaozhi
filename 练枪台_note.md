# 练枪台 小改动记录（11-22 晚）

## 待改
- [ ] 手机上按钮按下去要有反馈：加 `.btn:active{z-index/transform/底色变深}`，46px 高别动。
- [ ] touchstart 开枪已经加了，验证一下双触发（touchstart 后又 click）会不会一枪算两枪 → 加 `e.preventDefault()` 或 `if(e.touches)` 标记。
- [ ] 重开一把按钮位置：右下，别跟开枪键打架。

## 结论（待试玩后填）
- iPhone 上点得准不准：______
