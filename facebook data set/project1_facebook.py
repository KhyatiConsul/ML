#Ques1
import pandas as pd 
facebook_data = pd.read_csv('Facebook_Marketplace_data.csv')
facebook_data['hour'] = pd.to_datetime(facebook_data['status_published']).dt.hour
average_reactions_by_hour = facebook_data.groupby('hour')['num_reactions'].mean()
peak_hours = average_reactions_by_hour.idxmax()
print(f"peak hours: {peak_hours} and avg reactions: {average_reactions_by_hour[peak_hours]:.2f}")

#Ques2
correlation_reactions_comments = 
    facebook_data['num_reactions'].corr(facebook_data['num_comments'], method = 'spearman')
correlation_reactions_shares = 
    facebook_data['num_reactions'].corr(facebook_data['num_shares'], method='spearman')
print(f"Correlation (reactions vs comments): {correlation_reactions_comments:.2f}")
print(f"Correlation (reactions vs shares): {correlation_reactions_shares:.2f}")

#Ques3
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
features = facebook_data[['num_reactions', 'num_comments', 'num_shares', 'num_likes', 
                          'num_loves', 'num_wows', 'num_hahas', 'num_sads', 'num_angrys']]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
kmeans = KMeans(n_clusters = 3, random_state = 42)
clusters = kmeans.fit_predict(scaled_features)
facebook_data['cluster'] = clusters

#Ques4
import matplotlib.pyplot as plt 
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state= 42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)
plt.plot(range(1,11), inertia, marker = 'o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

#Ques5
post_counts = facebook_data['status_type'].value_counts()
print(post_counts)

#Ques6
averages_by_type = facebook_data.groupby('status_type')[['num_reactions', 'num_comments', 'num_shares']].mean()
print(averages_by_type)