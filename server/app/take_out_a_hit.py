from boto.mturk.connection import MTurkConnection
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
from keys import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, HOST

debug = False

def new_sugg_hit(PIN_IMAGE_URL, PIN_IMAGE_TITLE):
    
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
def new_rate_hit(PIN_IMAGE_URL, PIN_IMAGE_TITLE, MACYS_IMAGE_URL,MACYS_IMAGE_TITLE):
    mtc = MTurkConnection(aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          host=HOST)
                      
    if debug: print mtc.get_account_balance()

    title = 'Match these Pictures to Macy\'s Products'
    description = 'Look at this photo and match it to Macy\'s products'
    keywords = 'clothing, rating, opinions, easy, quick, macys'

    ratings =[('Very Bad','1'),
             ('Bad','2'),
             ('OK','3'),
             ('Good','4'),
             ('Very Good','5')]
 
    #make overview
 
    overview = Overview()
    overview.append_field('Title', 'Rank how these two images match.')
    overview.append(FormattedContent('<table border="1">><tr><td width="50%"><img src="'+PIN_IMAGE_URL+'" alt="Pintrest Image" /></td>'
                                     '<td width="50%"><img src="'+MACYS_IMAGE_URL+'" alt="Macys Image" /></td></tr><tr>'
                                     '<td width="50%">'+PIN_IMAGE_TITLE+'</td><td width="50%">'+MACYS_IMAGE_TITLE+'</td></tr></table>'))
    #make q1
 
    qc1 = QuestionContent()
    qc1.append_field('Title','Rank the match between these two')
 
    fta1 = SelectionAnswer(min=1, max=1,style='dropdown',
                          selections=ratings,
                          type='text',
                          other=False)
 
    q1 = Question(identifier='rating',
                  content=qc1,
                  answer_spec=AnswerSpecification(fta1),
                  is_required=True)
              
    #make q2
 
    qc2 = QuestionContent()
    qc2.append_field('Title','Comments about the HIT (Optional)')
 
    fta2 = FreeTextAnswer()
 
    q2 = Question(identifier="comments",
                  content=qc2,
                  answer_spec=AnswerSpecification(fta2))
 
    #make question form
 
    question_form = QuestionForm()
    question_form.append(overview)
    question_form.append(q1)
    question_form.append(q2)
 
    #--------------- CREATE THE HIT -------------------
 
    mtc.create_hit(questions=question_form,
                   max_assignments=1,
                   title=title,
                   description=description,
                   keywords=keywords,
                   duration = 60*5,
                   reward=0.05)
    