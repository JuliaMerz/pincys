from boto.mturk.connection import MTurkConnection
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
from keys import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

debug = True

HOST = 'mechanicalturk.sandbox.amazonaws.com'

PIN_IMAGE_URL = 'http://media-cache-ak0.pinimg.com/236x/17/8f/99/178f993435fb2718ab6e22ba29d704e0.jpg'
PIN_IMAGE_TITLE = 'Arnhem Clothing \'Song Bird\' Kimono in Mayan Song. Via Soleilblue..'


mtc = MTurkConnection(aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      host=HOST)
                      
if debug: print mtc.get_account_balance()


title = 'Match these Pictures to Macy\'s Products'
description = 'Look at this photo and match it to Macy\'s products'
keywords = 'clothing, rating, opinions, easy, quick, macys'
 
#make overview
 
overview = Overview()
overview.append_field('Title', 'Find three Macys.com Product Web IDs That Match')
overview.append(FormattedContent('<img src="'+PIN_IMAGE_URL+'" alt="Pintrest Image" />'
                                 '<br />'+PIN_IMAGE_TITLE))
               
#make webid1
 
qc1 = QuestionContent()
qc1.append_field('Title','First WebID Code')
 
fta1 = FreeTextAnswer(num_lines=1)
 
q1 = Question(identifier="FirstWebCode",
              content=qc1,
              answer_spec=AnswerSpecification(fta1))

#make webid2
 
qc2 = QuestionContent()
qc2.append_field('Title','Second WebID Code')
 
fta2 = FreeTextAnswer(num_lines=1)
 
q2 = Question(identifier="SecondWebCode",
              content=qc2,
              answer_spec=AnswerSpecification(fta2))
              
#make webid1
 
qc3 = QuestionContent()
qc3.append_field('Title','Third WebID Code')
 
fta3 = FreeTextAnswer(num_lines=1)
 
q3 = Question(identifier="ThirdWebCode",
              content=qc3,
              answer_spec=AnswerSpecification(fta3))
 
#make question form
 
question_form = QuestionForm()
question_form.append(overview)
question_form.append(q1)
question_form.append(q2)
question_form.append(q3)
 
#--------------- CREATE THE HIT -------------------
 
mtc.create_hit(questions=question_form,
               max_assignments=1,
               title=title,
               description=description,
               keywords=keywords,
               duration = 60*5,
               reward=0.05)

