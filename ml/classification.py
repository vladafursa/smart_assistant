import requests
from scipy.spatial.distance import cosine
from config import HUGGINGFACE_KEY
from ml import get_embeddings


API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2/pipeline/sentence-similarity"
headers = {
     "Authorization": f"Bearer {HUGGINGFACE_KEY}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


tech_examples = [
  "The app won't launch after the update",  # software crash
  "How do I reset the password in the access control system?",  # configuration
  "The device won't connect to Bluetooth",  # connectivity issue
  "I get a 500 error when logging into my account",  # server error
  "My laptop overheats and shuts down",  # hardware issue
  "How do I set up a VPN on my work computer?",  # configuration
  "The scanner isn't recognized by the system",  # driver/compatibility
  "Why isn't two-factor authentication working?",  # security failure
  "Notifications aren't showing up in the app",  # UI/UX bug
  "How do I install a graphics card driver?",  # software installation
  "The site froze during payment",  # technical glitch
  "I can't upload a file, it says 'network error'",  # network failure
  "My microphone doesn't work in Zoom even though it's connected",  # device issue
  "Why doesn't the 'Submit' button work on the form?",  # UI bug
  "How do I clear my browser cache?"  # technical instruction
]


cust_examples = [
  "I want to cancel my order, it hasn't been shipped yet",  # order management
  "I received the wrong item from what I ordered",  # delivery error
  "How can I change my payment method?",  # account/payment
  "Where can I find my bill from last month?",  # documentation
  "Can I get a refund if the item doesn't suit me?",  # return policy
  "Why is my account blocked?",  # access issue
  "How do I renew my subscription?",  # service management
  "I didn't receive the order confirmation email",  # communication
  "How long does delivery take?",  # logistics
  "How can I contact support about a return?",  # support
  "Payment failed but the money was withdrawn",  # financial incident
  "I want to complain about the service quality",  # feedback
  "Where can I view my order history?",  # customer interface
  "I didn't get loyalty points for my purchase",  # loyalty program
  "How do I change the delivery address?"  # logistics
]


talk_examples = [
  "How are you?",
  "Hi",
  "What's new?",
  "What's the weather like today?",
  "Can you speak Belarusian?",
  "What's your favorite movie?",
  "What do you think about the future?",
  "Are you real?",
  "How old are you?",
  "Can you tell a joke?"
]


tech_embeds = get_embeddings(tech_examples)
cust_embeds = get_embeddings(cust_examples)
small_embeds = get_embeddings(talk_examples)


def classify(query, threshold=0.3):
    query_vec = get_embeddings([query])[0]

    scores = {
        "tech_support": min(cosine(query_vec, vec) for vec in tech_embeds),
        "customer_support": min(cosine(query_vec, vec) for vec in cust_embeds),
        "small_talk": min(cosine(query_vec, vec) for vec in small_embeds),
    }

    best_category = min(scores, key=scores.get)
    best_score = scores[best_category]

    return best_category if best_score < threshold else "unknown"