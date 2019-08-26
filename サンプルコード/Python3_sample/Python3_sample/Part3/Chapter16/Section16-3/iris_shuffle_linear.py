from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import ShuffleSplit
# アヤメのデータセットを読み込む
iris = datasets.load_iris()
X = iris.data
y = iris.target
# データを分割するインデックスを作る
iris_ss = ShuffleSplit(n_splits=1, train_size=0.6, test_size=0.4, random_state=0)
train_index, test_index = next(iris_ss.split(X))
# データを分割する
X_train, y_train = X[train_index], y[train_index]    # 訓練データ
X_test, y_test = X[test_index], y[test_index]    # テストデータ
clf = linear_model.LogisticRegression()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))