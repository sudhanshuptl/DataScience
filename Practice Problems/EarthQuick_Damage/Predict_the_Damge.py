
# coding: utf-8

# # [Predict the damage to a building](https://www.hackerearth.com/challenge/competitive/machine-learning-challenge-6-1/machine-learning/predict-the-energy-used-612632a9-3f496e7f/)

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


train_p1 = pd.read_csv('./Dataset/train.csv')
test =pd.read_csv('./Dataset/test.csv')


# In[3]:


train_p1.head()


# In[4]:


test.head()


# In[5]:


print('train :',train_p1.shape)
print('Test :',test.shape)


# In[6]:


train_p2 = pd.read_csv('./Dataset/Building_Ownership_Use.csv')
train_p2.head()


# In[7]:


train_p2.shape


# # Note
#    * for few building id data is not in train_p1 
#    * that might be for test dataset so we gonna use inner join

# In[8]:


train_p1.loc[train_p1['building_id'] == 'a338a4e5f2' ]


# # find column columns

# In[9]:


col1 = train_p1.columns
col2 = train_p2.columns
comm_cols = []
for col in col1:
    if col in col2:
        comm_cols.append(col)
print(comm_cols)


# # join train_p1 and p2 as inner join

# In[10]:


train_p12 = pd.merge(train_p1,train_p2,how='inner',  left_on = ['building_id','district_id','vdcmun_id'],  right_on = ['building_id','district_id','vdcmun_id'])

test = pd.merge(test, train_p2, how='inner',   left_on = ['building_id','district_id','vdcmun_id'],    right_on = ['building_id','district_id','vdcmun_id'])


# In[11]:


train_p12.head()


# In[12]:


test.head()


# In[13]:


print('train :',train_p12.shape)
print('Test :',test.shape) #exactly same as data in train.csv


# In[14]:


#need to verify column merge correctly


# In[15]:


train_p12.loc[train_p12['building_id']=='a338a4e5f2']


# In[16]:


#dereferencing p1 and p2
del train_p1
del train_p2


# ## loading last part of dataset

# In[17]:


# loading last part of dataset
train_p3 = pd.read_csv('./Dataset/Building_Structure.csv')


# In[18]:


train_p3.head()


# In[19]:


train_p3.shape


# # Find common columns before merging

# In[20]:


col1 = train_p12.columns
col2 = train_p3.columns
comm_cols = []
for col in col1:
    if col in col2:
        comm_cols.append(col)
print(comm_cols)


# # Final Merge  

# In[21]:


train = pd.merge(train_p12,train_p3, how='inner',                  left_on=['building_id','district_id','vdcmun_id','ward_id'],                right_on=['building_id','district_id','vdcmun_id','ward_id'])

test = pd.merge(test,train_p3, how='inner',                  left_on=['building_id','district_id','vdcmun_id','ward_id'],                right_on=['building_id','district_id','vdcmun_id','ward_id'])


# In[22]:


print(train.shape)
train.head()


# In[23]:


print(test.shape)
test.head()


# In[24]:


del train_p12
del train_p3


# # Data is collected now Data Clinsing for Using Regression

# <h2> Problem Statement </h2>
# 
# <p>Determining the degree of damage that is done to buildings post an earthquake can help identify safe and unsafe buildings, thus avoiding death and injuries resulting from aftershocks.  Leveraging the power of machine learning is one viable option that can potentially prevent massive loss of lives while simultaneously making rescue efforts easy and efficient.</p>
# 
# <p>In this challenge we provide you with the before and after details of nearly one million buildings after an earthquake. The damage to a building is categorized in five grades. Each grade depicts the extent of damage done to a building post an earthquake.</p>
# 
# <p>Given building details, your task is to build a model that can predict the extent of damage that has been done to a building after an earthquake.</p>
# 
# <h2>Data Description:</h2>
# 
# <p>You’re give four files: train.csv, test.csv, Building_Ownership_Use.csv and Building_Structure.csv.</p>
# 
# <p>Details of the train.csv file:</p>
# 
# <table border="1">
# 	<tbody>
# 		<tr>
# 			<td>
# 			<p><strong>Variable</strong></p>
# 			</td>
# 			<td>
# 			<p><strong>Description</strong></p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>area_assesed</p>
# 			</td>
# 			<td>
# 			<p>Indicates the nature of the damage assessment in terms of the areas of the building that were assessed</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>building_id</p>
# 			</td>
# 			<td>
# 			<p>A unique ID that identifies every individual building</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>damage_grade</p>
# 			</td>
# 			<td>
# 			<p>Damage grade assigned to the building after assessment (Target Variable)</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>district_id</p>
# 			</td>
# 			<td>
# 			<p>District where the building is located</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>has_geotechnical_risk</p>
# 			</td>
# 			<td>
# 			<p>Indicates if building has geotechnical risks</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>has_geotechnical_risk_fault_crack</p>
# 			</td>
# 			<td>
# 			<p>Indicates if building has geotechnical risks related to fault cracking</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>has_geotechnical_risk_flood</p>
# 			</td>
# 			<td>
# 			<p>Indicates if building has geotechnical risks related to flood</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>has_geotechnical_risk_land_settlement</p>
# 			</td>
# 			<td>
# 			<p>Indicates if building has geotechnical risks related to land settlement</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>has_geotechnical_risk_landslide</p>
# 			</td>
# 			<td>
# 			<p>Indicates if building has geotechnical risks related to landslide</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>has_geotechnical_risk_liquefaction</p>
# 			</td>
# 			<td>
# 			<p>Indicates if building has geotechnical risks related to liquefaction</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>has_geotechnical_risk_other</p>
# 			</td>
# 			<td>
# 			<p>Indicates if building has any other  geotechnical risks</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>has_geotechnical_risk_rock_fall</p>
# 			</td>
# 			<td>
# 			<p>Indicates if building has geotechnical risks related to rock fall</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>has_repair_started</p>
# 			</td>
# 			<td>
# 			<p>Indicates if the repair work had started</p>
# 			</td>
# 		</tr>
# 		<tr>
# 			<td>
# 			<p>vdcmun_id</p>
# 			</td>
# 			<td>
# 			<p>Municipality where the building is located</p>
# 			</td>
# 		</tr>
# 	</tbody>
# </table>
# 
# <p>Details of the remaining files are described in the ReadMe file.</p>
# 
# <h2><a href="https://he-s3.s3.amazonaws.com/media/hackathon/machine-learning-challenge-6-1/predict-the-energy-used-612632a9-3f496e7f/a490e594-6-Dataset.zip" target="_blank">Download dataset</a></h2>
# 
# <h2><strong>Submission</strong></h2>
# 
# <p>A participant has to submit a zip file containing your ‘building_id’ and predicted ‘damage_grade’ in a csv format. Check the sample submission file for format.</p>
# 
# <pre class="prettyprint"><code>building_id, damage_grade
# a3380c4f75, Grade 3
# a338a4e653, Grade 1
# a338a4e6b7, Grade 1
# a33a6eaa3a, Grade 5
# a33b073ff6, Grade 4
# </code></pre>
# 
# 

# In[25]:


train.head()


# ## Replace grades with numbers only

# In[26]:


train['damage_grade'].unique()


# In[27]:


map_damage_grade={}
for key in train['damage_grade'].unique():
    if key not in map_damage_grade:
        map_damage_grade[key] = int(key[-1])

print(map_damage_grade)


# In[28]:


train['damage_grade'] = train['damage_grade'].replace(map_damage_grade)


# In[29]:


train.head()


# # replace area_assesed with numbers

# In[30]:


train['area_assesed'].unique()


# In[31]:


map_area_assesed = {'Interior':1,'Exterior':2,'Both':3,'Building removed':4}
# now assign 'Not able to inspect' as mean of values above


# In[32]:


pd.Series([x for x in map_area_assesed.values()]).describe()


# In[33]:


map_area_assesed['Not able to inspect'] = pd.Series([x for x in map_area_assesed.values()]).mean()
map_area_assesed


# In[34]:


test['area_assesed'] = test['area_assesed'].map(map_area_assesed)
train['area_assesed'] = train['area_assesed'].map(map_area_assesed)


# In[35]:


train.head()


# In[36]:


test.head()


# # Replace 'condition_post_eq'

# In[37]:


train['condition_post_eq'].unique()


# In[38]:


map_condition_post_eq = {}
count=1
for key in train['condition_post_eq'].unique():
    if key not in map_condition_post_eq:
        if key == 'Not damaged':
            map_condition_post_eq[key] = 0
        else:
            map_condition_post_eq[key] = count
            count +=1
print(map_condition_post_eq)


# In[39]:


test['condition_post_eq'] = test['condition_post_eq'].map(map_condition_post_eq)
train['condition_post_eq'] = train['condition_post_eq'].map(map_condition_post_eq)
train.head()


# In[40]:


test.head()


# # Need to fix All columns with object data type

# In[41]:


for col in train.columns:
    if train[col].dtype == train['legal_ownership_status'].dtype:
        print( col )


# ## legal_ownership_status replacement

# In[42]:


train['legal_ownership_status'].unique()


# In[43]:


train['legal_ownership_status'].head()


# In[44]:


map_legal_ownership_status = {'Private' : 1, 'Institutional':2,'Other':3,'Public':4 }
map_legal_ownership_status


# In[45]:


test['legal_ownership_status'] = test['legal_ownership_status'].map(map_legal_ownership_status)
train['legal_ownership_status'] = train['legal_ownership_status'].map(map_legal_ownership_status)


# In[46]:


test['legal_ownership_status'].head()


# In[47]:


test['legal_ownership_status'].dtype


# ## land_surface_condition conversion

# In[48]:


train['land_surface_condition'].unique()


# In[49]:


map_land_surface_condition = {'Flat':0, 'Moderate slope':1,'Steep slope':2}


# In[50]:


test['land_surface_condition'] = test['land_surface_condition'].map(map_land_surface_condition)
train['land_surface_condition'] = train['land_surface_condition'].map(map_land_surface_condition)


# In[51]:


test['land_surface_condition'].dtype


# In[52]:


train['land_surface_condition'].dtype


# ## Foundation_type conversion

# In[53]:


train['foundation_type'].unique()


# In[54]:


map_foundation_type = {'RC':0, 'Cement-Stone/Brick':1,'Other':2,'Mud mortar-Stone/Brick':3}


# In[55]:


test['foundation_type'] = test['foundation_type'].map(map_foundation_type)
train['foundation_type'] = train['foundation_type'].map(map_foundation_type)


# In[56]:


test['foundation_type'].dtype


# In[57]:


train['foundation_type'].dtype


#  # Roof_type conversion
# 
# 

# In[58]:


train['roof_type'].unique()


# In[59]:


map_roof_type = {'RCC/RB/RBC':2,'Bamboo/Timber-Heavy roof':1,'Bamboo/Timber-Light roof':0}


# In[60]:


test['roof_type'] = test['roof_type'].map(map_roof_type)
train['roof_type'] = train['roof_type'].map(map_roof_type)


# In[61]:


test['roof_type'].dtype


# In[62]:


train['roof_type'].dtype


# # ground_floor_type conversion

# In[63]:


train['ground_floor_type'].dtype #datatype is object


# In[64]:


train['ground_floor_type'].unique()


# In[65]:


map_ground_floor_type = {'RC':0,'Brick/Stone':1,'Timber':2,'Other':3,'Mud':4}


# In[66]:


test['ground_floor_type'] = test['ground_floor_type'].map(map_ground_floor_type)
train['ground_floor_type'] = train['ground_floor_type'].map(map_ground_floor_type)


# In[67]:


test['ground_floor_type'].dtype


# In[68]:


train['ground_floor_type'].dtype


# ## other_floor_type conversion

# In[69]:


train['other_floor_type'].dtype


# In[70]:


train['other_floor_type'].unique()


# In[71]:


map_other_floor_type = {'Not applicable':0,'RCC/RB/RBC':1,'Timber-Planck':2,'TImber/Bamboo-Mud':3}


# In[72]:


test['other_floor_type'] = test['other_floor_type'].map(map_other_floor_type)
train['other_floor_type'] = train['other_floor_type'].map(map_other_floor_type)


# In[73]:


train['other_floor_type'].dtype


# In[74]:


test['other_floor_type'].dtype


# # position Conversion

# In[75]:


train['position'].dtype


# In[76]:


train['position'].unique()


# In[77]:


map_position ={'Not attached':1,'Attached-1 side':2,'Attached-2 side':3,'Attached-3 side':4}


# In[78]:


test['position'] = test['position'].map(map_position)
train['position'] = train['position'].map(map_position)


# In[79]:


train['position'].dtype


# In[80]:


test['position'].dtype


# ## plan_configuration conversion

# In[81]:


train['plan_configuration'].dtype


# In[82]:


train['plan_configuration'].unique()


# In[83]:


map_plan_configuration={}
count=1
for col in train['plan_configuration'].unique():
    if col not in map_plan_configuration:
        map_plan_configuration[col] = count
        count +=1
map_plan_configuration


# In[84]:


test['plan_configuration'] = test['plan_configuration'].map(map_plan_configuration)
train['plan_configuration'] = train['plan_configuration'].map(map_plan_configuration)


# In[85]:


train['plan_configuration'].dtype


# In[86]:


test['plan_configuration'].dtype


# # Checking All columns are int or floa not object

# In[87]:


for col in train.columns:
    print(train[col].dtype)


# # Remove All NanN or infinite

# ## Fill NanN by Mean of that column

# In[91]:


train.head()


# In[92]:


map_nan = {np.nan:train['district_id'].mean(),np.inf:train['district_id'].max()}
map_nan


# In[93]:


train['district_id']=train['district_id'].replace(map_nan)


# In[96]:


# generic For All columns
map_all={} #dict of dict
for col in train.columns:
    if col != 'building_id':
        map_all[col]={np.nan:train[col].mean(),np.inf:train[col].max()}
map_all


# In[99]:


#replace infinity and nan from train datafram
for col in map_all:
    train[col]=train[col].replace(map_all[col])


# In[102]:


#replace infinity and nan from test datafram
for col in map_all:
    if col !='damage_grade':
        test[col]=test[col].replace(map_all[col])


# In[103]:


train.head()


# # Training And Testing Without Normalization

# In[104]:


columns_dont_want_in_train_x = ['building_id','damage_grade']
features_col = [col for col in train.columns if col not in columns_dont_want_in_train_x ]
print(features_col)

train_x = np.array(train.loc[:,features_col])


# In[105]:


test_x = np.array(test.loc[:,features_col])


# In[106]:


train_x


# In[107]:


train_x.shape


# In[108]:


print(test_x.shape)
test_x


# In[109]:


train_y =  np.array(train.loc[:,'damage_grade'])
train_y.shape


# In[110]:


train_y[:10]


# # Classifier

# In[111]:


from sklearn import svm


# In[112]:


clsf = svm.SVC()
clsf


# In[ ]:


clsf.fit(train_x,train_y)


from sklearn.externals import joblib
joblib.dump(clsf, 'filename.pkl')

print('Hii I am DOne')