import pickle
from sklearn.cluster import MiniBatchKMeans
from flask import Flask, render_template,request
model=pickle.load(open('model.pkl','rb'))
one = model[0]
two = model[1]
three = model[2]
four = model[3]
five = model[4]
six = model[5]
seven = model[6]
eight = model[7]
nine = model[8]
ten = model[9]
all_types_scores = {'one':one, 'two': two, 'three' :three, 'four':four, 'five':five, 'six': six, 'seven': seven, 'eight': eight,
             'nine': nine, 'ten': ten}
for name, personality_type in all_types_scores.items():
    personality_trait = {}

    personality_trait['extroversion_score'] =  personality_type[0] - personality_type[1] +personality_type[2] - personality_type[3] + personality_type[4] - personality_type[5] +personality_type[6] - personality_type[7] + personality_type[8] -personality_type[9]
    personality_trait['neuroticism_score'] =  personality_type[10] - personality_type[11] + personality_type[12] -personality_type[13] + personality_type[14] + personality_type[15] + personality_type[16] + personality_type[17] + personality_type[18] + personality_type[19]
    personality_trait['agreeableness_score'] =  -personality_type[20] +personality_type[21] - personality_type[22] + personality_type[23] - personality_type[24] - personality_type[25] + personality_type[26] - personality_type[27] + personality_type[28] + personality_type[29]
    personality_trait['conscientiousness_score'] = personality_type[30] - personality_type[31] + personality_type[32] -personality_type[33] +personality_type[24] - personality_type[35] +personality_type[36] -personality_type[37] + personality_type[38] + personality_type[39]
    personality_trait['openness_score'] =  personality_type[40] -personality_type[41] + personality_type[42] - personality_type[43] + personality_type[34] - personality_type[45] +personality_type[46] + personality_type[47] + personality_type[48] + personality_type[49]
    all_types_scores[name] = personality_trait
all_extroversion = []
all_neuroticism =[]
all_agreeableness =[]
all_conscientiousness =[]
all_openness =[]

for personality_type, personality_trait in all_types_scores.items():
    all_extroversion.append(personality_trait['extroversion_score'])
    all_neuroticism.append(personality_trait['neuroticism_score'])
    all_agreeableness.append(personality_trait['agreeableness_score'])
    all_conscientiousness.append(personality_trait['conscientiousness_score'])
    all_openness.append(personality_trait['openness_score'])

all_extroversion_normalized = (all_extroversion-min(all_extroversion))/(max(all_extroversion)-min(all_extroversion))
all_neuroticism_normalized = (all_neuroticism-min(all_neuroticism))/(max(all_neuroticism)-min(all_neuroticism))
all_agreeableness_normalized = (all_agreeableness-min(all_agreeableness))/(max(all_agreeableness)-min(all_agreeableness))
all_conscientiousness_normalized = (all_conscientiousness-min(all_conscientiousness))/(max(all_conscientiousness)-min(all_conscientiousness))
all_openness_normalized = (all_openness-min(all_openness))/(max(all_openness)-min(all_openness))
all_normalized=[]
all_normalized.append(all_extroversion_normalized.tolist())
all_normalized.append(all_neuroticism_normalized.tolist())
all_normalized.append(all_agreeableness_normalized.tolist())
all_normalized.append(all_conscientiousness_normalized.tolist())
all_normalized.append(all_extroversion_normalized.tolist())
all_types_scores = {'one':[], 'two': [], 'three' :[], 'four':[], 'five':[], 'six': [], 'seven':[], 'eight': [],
             'nine': [], 'ten': []}
l=['one','two','three','four','five','six','seven','eight','nine','ten']
k=[[] for i in range(10)]

for j in all_normalized:
    for i in range(10):
        all_types_scores[l[i]].append(j[i])
        k[i].append(j[i])
all_normalized=k
print('all_normalized',all_normalized)
app = Flask(__name__)
@app.route('/' , methods=['GET', 'POST'])
def index():
    name_of_slider = request.form.getlist('hello[]')
    
    
    return render_template('input.html',**locals())
    
@app.route("/test" , methods=['GET', 'POST'])

def test():
    arr = list(request.form.values())
    print('arr',arr)
    arr_scores,your_output_scores={},[]
    behaviour_list=['Extroversion','Neuroticism','Agreeableness','Conscientiousness','Openness']
    arr_scores['extroversion_score'] =  float(arr[0]) - float(arr[1]) +float(arr[2])-float(arr[3])
    arr_scores['neuroticism_score'] =  float(arr[4])- float(arr[5]) + float(arr[6])-float(arr[7])
    arr_scores['agreeableness_score'] =  -float(arr[8]) +float(arr[9])- float(arr[10]) + float(arr[11])
    arr_scores['conscientiousness_score'] = float(arr[12]) - float(arr[13]) + float(arr[14]) -float(arr[15])
    arr_scores['openness_score'] =  float(arr[16] )-float(arr[17] )+ float(arr[18]) - float(arr[19])
    print('aftercal',arr_scores)
    for i,j in arr_scores.items():
        k=arr_scores[i]
        if k<=0:
            arr_scores[i]=0
            your_output_scores.append(arr_scores[i])
        else:
            arr_scores[i]=(k*2)/100
            your_output_scores.append(arr_scores[i])
    index_list=[]
    print('your_output_scores',your_output_scores)
    print('arr_scores',arr_scores)
    dom,weak=your_output_scores.index(max(your_output_scores)),your_output_scores.index(min(your_output_scores))
    dominate=behaviour_list[dom]
    weaker=behaviour_list[weak]

    diff=[]
    for i in range(10):
        k=sum([abs(all_normalized[i][j]-your_output_scores[j]) for j in range(5)])
        diff.append(k)
    print('k',diff)
    behaviour=diff.index(min(diff))
    type=''
    if behaviour==0:
        type='Type A: Extrovert'
    elif behaviour==1:
        type='Type B: Introvert'
    elif behaviour==2:
        type='Type C: Delirious'
    elif behaviour==3:
        type='Type D: Calm'
    elif behaviour==4:
        type='Type E: Agreeable'
    elif behaviour==5:
        type='Type F: Antagonistic'
    elif behaviour==6:
        type='Type G: Conscientious'
    elif behaviour==7:
        type='Type H: Unprincipled'
    elif behaviour==8:
        type='Type I: Open'
    elif behaviour==9:
        type='Type J: Secretive'
    else:
        print("Please rerun the program!")
    print ("Your type is :",type)
    #yourtypelistacctoML
    type_list=[]
    for q in range(5):
        k=all_normalized[q][behaviour]
        type_list.append(k)

    print(type_list)
    return render_template('output.html',type_list=type_list,type=type,dominate=dominate,weaker=weaker)

 
app.run(debug=True)