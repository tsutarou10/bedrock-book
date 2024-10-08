# 第２章 Amazon Bedrock 入門

- メリット
  - さまざまな会社が提供する生成AIのモデルをサーバレスで利用可能
- なぜ Bedrock をえらぶのか
  - AWS の強みの多くを享受できる
    - 利用者による知見のアプトプットが盛んである
    - 習熟したスキルを持つ開発者が多く、人材を探しやすい
    - 既存の AWS システムに、容易に生成 AI を組み込むことができる
    - サポートの品質が高い
  - 複数の会社が提供する最先端モデルを幅広く利用できる
    - Anthropic (Claude): テキスト生成の主力
    - Cohere (Command, Embed): 埋め込み品質に定評
    - Stability AI (SDXL): 画像生成の主力
    - Amazon (Titan): AWS 自社モデル
      - 使用中のモデルが何らかの理由で突然利用できなくなっても、Titan シリーズへの切り替えが常に可能
    - Meta (Llama): 公開モデルの定番
  - アプリケーション開発との親和性が高い
    - アプリケーションを便利に開発するための「マネージドサービス」が豊富
      - 社内文書検索の実現
        - 本来は、社内文書を検索してLLM のプロンプトに付加するための複雑な処理を実装し、それを稼働させるサーバ構築・運用が必要
        - Knowledge bases for Amazon Bedrock を使えば同様の機能を実現できる
  - エンタープライズ環境での本番利用に耐えうる高いセキュリティとガバナンスが提供されている
    - 生成 AI もでるに送信した企業独自のデータが他の利用者に見られたり、モデル提供企業によってデータ学習用途に使われたりすることはない
    - Bedrock は、ISO, SOC といった一般的なコンプライアンス基準の対象となっている
    - HIPAA (医療保険の相互運用性と説明責任に関する法律) や GDPR にも準拠している
- モデルの種類
  - テキスト生成
  - 埋め込み
  - 画像生成
- モデルの有効化
  - https://zenn.dev/k_tamu/articles/98f3052dbfb4ac#%E3%81%BE%E3%81%9A%E3%81%AFamazon-bedrock%E3%82%92%E9%96%8B%E3%81%84%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86
- Playground でチャットを試してみる
  - 画像
- Claude の API の推論パラメータ
  - temperature
    - 0 ~ 1 (default: 1)
      - 値が高いほど、出力結果がランダム性を帯びるようになる
      - 分析や多肢選択問題への回答タスクには低い値、創造的なタスクには高い値を使用することが推奨される
    - top_p: 0 ~ 1 (default: 0.999)
      - トークン生成時にサンプリングする範囲を指定する値
      - temperature と top_p はどちらか一方だけを調整し、一般的な用途には temperature を調整することが推奨される
    - top_k: 0 ~ 500 (defualt: 250)
      - トークン生成時にサンプリングする個数を制限する値
      - top_p 同様、一般的な用途には temperature を調整することが推奨される
- AWS SDK 用いて各モデルのAPIへリクエストを行う方法

  - テキスト生成

    - https://github.com/minorun365/bedrock-book/blob/main/chapter2/2_invoke-model.py

    ```shell
    ベドロックには主に以下の2つの意味があります。

    1. 地質学的な意味
    堅固で侵食されにくい基盤岩のことを指します。地層の最下部にあり、その上に堆積岩層が積み重なっています。

    2. 比喩的な意味
    何かの根本的な基礎や礎を表す言葉として使われます。例えば、
    「この理論は研究のベドロックとなっている」など、重要な基盤となる部分を指して使います。

    転じて、頑健で揺るぎない土台や基礎という意味合いも持ちます。堅牢で動じないという強固さを表現する言葉として使われるのです。

    コンピューターゲーム「Minecraft」でも、ベドロックは地下世界の最下層を構成する壊すことのできない岩盤層のことを指しています
    ```

  - ストリーミングでテキスト生成
    - <3_streaming.py の実行動画>
  - マルチモーダル入力でテキスト生成を行う
    - <4_multimodal.py の実行結果>
