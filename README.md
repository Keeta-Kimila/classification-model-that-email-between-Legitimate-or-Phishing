# Classification model that email between Legitimate or Phishing
This is project aim for classification which email are Legitimate or Phishing.

## Deploy web app via [streamlit.io](https://streamlit.io/#install)
<b>Web app</b>: https://classification-model-that-email-between-legitimate-or-phishing.streamlit.app/

List model that used within web app:
- XGBoost
- SVM+XGBoost
- LightGBM

Note that: <b>roberta base</b> is the <b>best model</b> in this case but size of <b>model too large</b>, so we can't deploy within web app and put model file in this github.
# Data Availability
- The AI-Generated Emails dataset supporting the findings of this study, publicly accessible via the kaggle of Opara at https://www.kaggle.com/datasets/guchiopara/ai-generated-emails, accessed on Nov 14, 2025.
- The pre-trained roberta-base model used in this study is publicly available via the huggingface of FacebookAI at https://huggingface.co/FacebookAI/roberta-base, accessed on Nov 20, 2025.


# Refer (Paper)
C. Opara, P. Modesti, and L. Golightly, “Evaluating spam filters and stylometric detection of
ai-generated phishing emails,” Expert Systems with Applications, vol. 276, p. 127044, 2025.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/S0957417425006669
