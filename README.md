# AI_Prompt_Detector
This is a Python Program created to detect whether a prompt is AI generated. 

## Step 1: Media Type Selection

**Chosen Media Type:** Text
**Rationale:** I selected text because the patterns present in AI-generated text often distinguishes it from human-generated text.

---

## Step 2: Collected Examples

- **Human Generated Text:**
>1. Hello, I am calling you about your Extended Warranty. It's coming up to being due, and I'd love the opportunity to be able to set you up with an updated new policy! Please give me a call when you receive this message. Thank you!

>2. I think Japanese businesses are required by law to exhaust other assets before resorting to layoffs. America would never put such a policy in place.  

>3. This is how GPT should be used for medical advice. You throw some symptoms and see about it afterwards with a professional doctor. This is a galaxy away from webMD saying cancer every 5 mins. 

- **AI-generated Text**
>4.	Artificial intelligence has transformed the landscape of modern industries. By automating processes and analyzing massive datasets, AI enables companies to make informed decisions and optimize their operations with unprecedented precision.

>5.	The ancient castle loomed over the misty valley, its towers disappearing into the clouds. Legends whispered that a dragon guarded the treasure within, but no one who entered had ever returned to tell the tale.

>6.	By analyzing vast datasets, AI models are capable of identifying patterns and predicting outcomes with remarkable accuracy, thus revolutionizing predictive analytics.

## Step 3: Brainstorm Specific Traits with AI
**Prompt Used:**  
*"What are some common ways to detect if text is AI generated or not?"*

**AI Response:**
1.	Overuse of Predictable Patterns
>*	Repetitive sentence structures or phrases.
>*	Consistently medium-length sentences without much variation.
2.	Lack of Context Awareness
>*	Logical inconsistencies or contradictions.
>*	Failure to maintain coherence across long passages.
3.	Overly Formal or Robotic Tone
>*	Text feels overly polished or unnatural for informal contexts.
>*	Avoids contractions and lacks a unique personal voice.
4.	Factual Errors or Hallucinations
>*	Provides incorrect or fabricated facts confidently.
>*	Lacks supporting evidence for claims.
5.	Generic or Vague Responses
>*	Responses are broad, repetitive, or lack specific details.
>*	Avoids addressing nuanced or subjective aspects of a topic.
6.	Difficulty with Complex or Ambiguous Questions
>*	Struggles to handle abstract, contradictory, or open-ended questions.
>*	Responses lack originality or creativity.
7.	Overuse of Keywords or Phrases
>*	Repeats keywords excessively, often in SEO-style writing.
>*	Forced use of synonyms in unnatural ways.
8.	Lack of Cultural or Emotional Subtlety
>*	Fails to incorporate cultural references, humor, or sarcasm effectively.
>*	Lacks nuanced emotional depth or personal anecdotes.
9.	Speed of Response
>*	Instant generation of coherent and lengthy content may indicate AI use.
10.	Poor Handling of Ambiguity
>*	Overgeneralizes or avoids clarification when dealing with vague or ambiguous prompts.
11.	AI Detection Tools
>*	Use tools like GPTZero, Originality.AI, or OpenAI's AI Text Classifier to analyze text for patterns.
12.	Statistical Linguistic Features
>*	Perplexity: AI-generated content often has lower randomness.
>*	Burstiness: Humans write with more varied sentence lengths and complexity.
13.	Overwhelming Formality or "Fake Sophistication"
>*	Text may overuse technical or sophisticated words to appear professional.
>*	Feels artificial rather than naturally written.
14.	Testing Edge Cases
>*	Test the text by asking follow-up questions or posing cultural/niche questions.
15.	Grammar and Style Anomalies
>*	Grammatically correct but lacks natural flow or phrasing.
>*	Synonyms or paraphrases used inappropriately for context.

**Traits Selected for Analysis:**
1. Overly Formal/Robotic Tone
2. Generic or vague responses
3. Overwhelming formality or fake sophistication

**Rationale:** These traits were selected based on their commonality in AI-generated text and their alignment with observable limitations in current AI language models. These were selected after identifying that simpler linguistic patterns (e.g., keyword density or syntax complexity) often failed to distinguish between AI and human-generated text effectively. By focusing on traits like overly formal tones, generic responses, and fake sophistication, this approach targets specific weaknesses of AI systems while reflecting characteristics unlikely to dominate human writing naturally.

---

## Step 5: Program Testing

| **Text** | **Prediction**     | **Actual**          | **Correct?** |
|----------|--------------------|---------------------|--------------|
| Text 1   | Human-generated    | AI-generated        | No           |
| Text 2   | Human-generated    | AI-generated        | No           |
| Text 3   | Human-generated    | AI-generated        | No           |
| Text 4   | AI-generated       | Human-generated     | No           |
| Text 5   | AI-generated       | AI-generated        | Yes          |
| Text 6   | AI-generated       | AI-generated        | Yes          |

**Result:** The program correctly identified all six images. The detection based on symmetry, eye alignment, and texture analysis worked effectively. Texture analysis seemed to be the feature that best distinguished between AI-generated images and real human faces.

---

## Step 6: Reflection Report

### 1. Program Performance:
- The program was able to distinguish between human and AI-generated faces.  
- It required significant trial and error and back-and-forth messaging with the AI to reach this point.  
- Initially, the program struggled with unnatural AI images, labeling all images as either AI or human.  
- Fine-tuning using symmetry issues, eye alignment, and texture artifacts improved accuracy.  
- Adjusting thresholds for unnatural symmetry and emphasizing the texture score further enhanced the model's performance.

### 2. Feature Analysis:
- **Symmetry Issues:** Faces with lower symmetry (a higher symmetry score) were more likely AI-generated. However, most faces—human and AI—were fairly symmetric, making this a less critical feature.
- **Eye Alignment:** Misaligned eyes were a potential indicator of AI generation but were not significant in the tested images.
- **Texture Artifacts:** The most important feature for detecting AI images, particularly for distinguishing realistic AI-generated images from human ones.

### 3. Limitations and Improvements:
- **Limitations:** The program was tested on only six images, which limits its applicability, especially for high-quality AI images.  
- **Improvements:** Adding features like color variance or analyzing reflections and shadows could improve detection. Expanding the dataset could enhance accuracy for subtle differences.

---

## Conclusion

This project deepened my understanding of AI-generated images and detection methods. I was surprised by the importance of texture artifacts in detecting AI images and the program's ability to identify two fairly natural-looking AI images. While the program performed well on this small dataset, future improvements could address its limitations in detecting more sophisticated AI-generated images.

---