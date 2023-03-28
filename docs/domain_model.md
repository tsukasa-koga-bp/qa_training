# ドメインモデル

## システム全体像


## 配送イメージ
![My alt text](map.drawio)


## モデリング
``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```