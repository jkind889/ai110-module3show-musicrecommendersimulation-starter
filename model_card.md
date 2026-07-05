# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)   Genre Enegry Mood
- What user preferences are considered  Favorite Genre, Favorite Mood,Target Energy and Likes acoustic
- How does the model turn those into a score  We check if the mood/genre matches the user's favorite genre and then add a point from there, as well as taking the energy gap and then multiplying that gap by 25 since it will be most likely be an decimal
- What changes did you make from the starter logic  - Mostly weighted towards genres

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog?  19
- What genres or moods are represented?  pop,lofi,rock,ambient,jazz
- Did you add or remove data?  I mostly added data
- Are there parts of musical taste missing in the dataset?  I think something like pluggnb could be included

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

It seems to work well when matching genres as well as rewarding matching genres since alot of people listen to music based off certain genres

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

It doesn't consider things like length and it overprioritizses genre more than anything else, for someone who only listens to one genre it'd be pretty good for them

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.


I tested user profiles such as genre lover, energy chaser, and someone whose in an acoustic mood
I was surprised the genre user profile not only matched genres but also gave reasonings due to energy levels being close to target, but of course a matching genre would dominate everything

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I'd probably add some UI for this as well as more options in the data and being able to classify recommendations without a genre and mood since it relates to a current project I'm working on

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned how some of these major recommender system works, I'm interested in applying some of this logic towards the current project i've been working on