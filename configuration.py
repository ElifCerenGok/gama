import numpy as np

# Last tested minimal configuration.
configuration_with_preprocessing = {
    'sklearn.tree.DecisionTreeClassifier': {
        'criterion': ["gini", "entropy"],
        'max_depth': range(1, 11),
        'min_samples_split': range(2, 21),
        'min_samples_leaf': range(1, 21)
    },
    
    'sklearn.naive_bayes.BernoulliNB': {
        'alpha': [1e-3, 1e-2, 1e-1, 1., 10., 100.],
        'fit_prior': [True, False]
    },
    
    'sklearn.preprocessing.Normalizer': {
        'norm': ['l1', 'l2', 'max']
    }
}


# Default TPOT Classifier config - only used for testing.
tpot_config = {

    # Classifiers
    'sklearn.naive_bayes.GaussianNB': {
    },

    'sklearn.naive_bayes.BernoulliNB': {
        'alpha': [1e-3, 1e-2, 1e-1, 1., 10., 100.],
        'fit_prior': [True, False]
    },

    'sklearn.naive_bayes.MultinomialNB': {
        'alpha': [1e-3, 1e-2, 1e-1, 1., 10., 100.],
        'fit_prior': [True, False]
    },

    'sklearn.tree.DecisionTreeClassifier': {
        'criterion': ["gini", "entropy"],
        'max_depth': range(1, 11),
        'min_samples_split': range(2, 21),
        'min_samples_leaf': range(1, 21)
    },

    'sklearn.ensemble.ExtraTreesClassifier': {
        'n_estimators': [100],
        'criterion': ["gini", "entropy"],
        'max_features': np.arange(0.05, 1.01, 0.05),
        'min_samples_split': range(2, 21),
        'min_samples_leaf': range(1, 21),
        'bootstrap': [True, False]
    },

    'sklearn.ensemble.RandomForestClassifier': {
        'n_estimators': [100],
        'criterion': ["gini", "entropy"],
        'max_features': np.arange(0.05, 1.01, 0.05),
        'min_samples_split': range(2, 21),
        'min_samples_leaf':  range(1, 21),
        'bootstrap': [True, False]
    },

    'sklearn.ensemble.GradientBoostingClassifier': {
        'n_estimators': [100],
        'learning_rate': [1e-3, 1e-2, 1e-1, 0.5, 1.],
        'max_depth': range(1, 11),
        'min_samples_split': range(2, 21),
        'min_samples_leaf': range(1, 21),
        'subsample': np.arange(0.05, 1.01, 0.05),
        'max_features': np.arange(0.05, 1.01, 0.05)
    },

    'sklearn.neighbors.KNeighborsClassifier': {
        'n_neighbors': range(1, 101),
        'weights': ["uniform", "distance"],
        'p': [1, 2]
    },

    'sklearn.svm.LinearSVC': {
        'penalty': ["l1", "l2"],
        'loss': ["hinge", "squared_hinge"],
        'dual': [False], # False
        'tol': [1e-5, 1e-4, 1e-3, 1e-2, 1e-1],
        'C': [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1., 5., 10., 15., 20., 25.]
    },

    'sklearn.linear_model.LogisticRegression': {
        'penalty': ["l1", "l2"],
        'C': [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1., 5., 10., 15., 20., 25.],
        'dual': [False] #,True
    },

    #'xgboost.XGBClassifier': {
    #    'n_estimators': [100],
    #    'max_depth': range(1, 11),
    #    'learning_rate': [1e-3, 1e-2, 1e-1, 0.5, 1.],
    #    'subsample': np.arange(0.05, 1.01, 0.05),
    #    'min_child_weight': range(1, 21),
    #    'nthread': [1]
    #},

    # Preprocesssors
    'sklearn.preprocessing.Binarizer': {
        'threshold': np.arange(0.0, 1.01, 0.05)
    },

    'sklearn.decomposition.FastICA': {
        'tol': np.arange(0.0, 1.01, 0.05)
    },

    'sklearn.cluster.FeatureAgglomeration': {
        'linkage': ['ward', 'complete', 'average'],
        'affinity': ['euclidean', 'l1', 'l2', 'manhattan', 'cosine', 'precomputed']
    },

    'sklearn.preprocessing.MaxAbsScaler': {
    },

    'sklearn.preprocessing.MinMaxScaler': {
    },

    'sklearn.preprocessing.Normalizer': {
        'norm': ['l1', 'l2', 'max']
    },

    'sklearn.kernel_approximation.Nystroem': {
        'kernel': ['rbf', 'cosine', 'chi2', 'laplacian', 'polynomial', 'poly', 'linear', 'additive_chi2', 'sigmoid'],
        'gamma': np.arange(0.0, 1.01, 0.05),
        'n_components': range(1, 11)
    },

    'sklearn.decomposition.PCA': {
        'svd_solver': ['randomized'],
        'iterated_power': range(1, 11)
    },

    'sklearn.preprocessing.PolynomialFeatures': {
        'degree': [2],
        'include_bias': [False],
        'interaction_only': [False]
    },

    'sklearn.kernel_approximation.RBFSampler': {
        'gamma': np.arange(0.0, 1.01, 0.05)
    },

    'sklearn.preprocessing.RobustScaler': {
    },

    'sklearn.preprocessing.StandardScaler': {
    },

    #'tpot.builtins.ZeroCount': {
    #},

    #'tpot.builtins.OneHotEncoder': {
    #    'minimum_fraction': [0.05, 0.1, 0.15, 0.2, 0.25],
    #    'sparse': [False]
    #},

    # Selectors
    'sklearn.feature_selection.SelectFwe': {
        'alpha': np.arange(0, 0.05, 0.001),
        'score_func': {
            'sklearn.feature_selection.f_classif': None
        }
    },

    'sklearn.feature_selection.SelectPercentile': {
        'percentile': range(1, 100),
        'score_func': {
            'sklearn.feature_selection.f_classif': None
        }
    },

    'sklearn.feature_selection.VarianceThreshold': {
        'threshold': np.arange(0.05, 1.01, 0.05)
    },

    'sklearn.feature_selection.RFE': {
        'step': np.arange(0.05, 1.01, 0.05),
        'estimator': {
            'sklearn.ensemble.ExtraTreesClassifier': {
                'n_estimators': [100],
                'criterion': ['gini', 'entropy'],
                'max_features': np.arange(0.05, 1.01, 0.05)
            }
        }
    },

    'sklearn.feature_selection.SelectFromModel': {
        'threshold': np.arange(0, 1.01, 0.05),
        'estimator': {
            'sklearn.ensemble.ExtraTreesClassifier': {
                'n_estimators': [100],
                'criterion': ['gini', 'entropy'],
                'max_features': np.arange(0.05, 1.01, 0.05)
            }
        }
    }

}

from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import FeatureAgglomeration
from sklearn.preprocessing import MaxAbsScaler, MinMaxScaler, Normalizer, PolynomialFeatures, RobustScaler, StandardScaler, Binarizer
from sklearn.kernel_approximation import Nystroem, RBFSampler
from sklearn.decomposition import PCA, FastICA
from sklearn.feature_selection import SelectFwe, SelectPercentile, f_classif, VarianceThreshold, RFE, SelectFromModel

# Default TPOT Classifier config - only used for testing.

new_config = {

    'alpha' : [1e-3, 1e-2, 1e-1, 1., 10., 100.],
    'fit_prior': [True, False],
    'min_samples_split': range(2, 21),
    'min_samples_leaf': range(1, 21),  
    
    # Classifiers
    GaussianNB: {
    },

    BernoulliNB: {
        'alpha': [],
        'fit_prior': []
    },

    MultinomialNB: {
        'alpha': [],
        'fit_prior': []
    },

    DecisionTreeClassifier: {
        'criterion': ["gini", "entropy"],
        'max_depth': range(1, 11),
        'min_samples_split': [],
        'min_samples_leaf': []
    },

    ExtraTreesClassifier: {
        'n_estimators': [100],
        'criterion': ["gini", "entropy"],
        'max_features': np.arange(0.05, 1.01, 0.05),
        'min_samples_split': [],
        'min_samples_leaf': [],
        'bootstrap': [True, False]
    },
    
    RandomForestClassifier: {
        'n_estimators': [100],
        'criterion': ["gini", "entropy"],
        'max_features': np.arange(0.05, 1.01, 0.05),
        'min_samples_split': range(2, 21),
        'min_samples_leaf':  range(1, 21),
        'bootstrap': [True, False]
    },

    GradientBoostingClassifier: {
        'n_estimators': [100],
        'learning_rate': [1e-3, 1e-2, 1e-1, 0.5, 1.],
        'max_depth': range(1, 11),
        'min_samples_split': range(2, 21),
        'min_samples_leaf': range(1, 21),
        'subsample': np.arange(0.05, 1.01, 0.05),
        'max_features': np.arange(0.05, 1.01, 0.05)
    },

    KNeighborsClassifier: {
        'n_neighbors': range(1, 51),
        'weights': ["uniform", "distance"],
        'p': [1, 2]
    },

    LinearSVC: {
        'penalty': ["l1", "l2"],
        'loss': ["hinge", "squared_hinge"],
        'dual': [False, True], 
        'tol': [1e-5, 1e-4, 1e-3, 1e-2, 1e-1],
        'C': [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1., 5., 10., 15., 20., 25.],
        'param_check': [lambda params: (not params['dual'] or params['penalty'] == "l2")
                                        and not (params['penalty'] == "l1" and params['loss'] == "hinge")
                                        and not (params['penalty'] == "l2" and params['loss'] == "hinge" and not params['dual']) ]
        #'param_check': [lambda params: ( not params['dual']
         #       (not params['dual'] or params['penalty'] == "l2")
         #                                and (params['penalty'] == "l1" and params['penalty'] == "squared_hinge")]
    },
    
    LogisticRegression: {
        'penalty': ["l1", "l2"],
        'C': [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1., 5., 10., 15., 20., 25.],
        'dual': [False, True],
        'param_check': [lambda params: not params['dual'] or params['penalty'] == "l2"]
    },

    #'xgboost.XGBClassifier': {
    #    'n_estimators': [100],
    #    'max_depth': range(1, 11),
    #    'learning_rate': [1e-3, 1e-2, 1e-1, 0.5, 1.],
    #    'subsample': np.arange(0.05, 1.01, 0.05),
    #    'min_child_weight': range(1, 21),
    #    'nthread': [1]
    #},
    
    # Preprocesssors
    Binarizer: {
        'threshold': np.arange(0.0, 1.01, 0.05)
    },

    FastICA: {
        'tol': np.arange(0.0, 1.01, 0.05)
    },

    FeatureAgglomeration: {
        'linkage': ['ward', 'complete', 'average'],
        'affinity': ['euclidean', 'l1', 'l2', 'manhattan', 'cosine', 'precomputed'],
        'param_check': [lambda params: (not params['linkage'] == "ward") or params['affinity'] == "euclidean"]
    },
    
    MaxAbsScaler: {
    },
    
    MinMaxScaler: {
    },
    
    Normalizer: {
        'norm': ['l1', 'l2', 'max']
    },
    
    Nystroem: {
        'kernel': ['rbf', 'cosine', 'chi2', 'laplacian', 'polynomial', 'poly', 'linear', 'additive_chi2', 'sigmoid'],
        'gamma': np.arange(0.0, 1.01, 0.05),
        'n_components': range(1, 11)
    },
    
    PCA: {
        'svd_solver': ['randomized'],
        'iterated_power': range(1, 11)
    },
    
    PolynomialFeatures: {
        'degree': [2],
        'include_bias': [False],
        'interaction_only': [False]
    },
    
    RBFSampler: {
        'gamma': np.arange(0.0, 1.01, 0.05)
    },
    
    RobustScaler: {
    },
    
    StandardScaler: {
    },
    
    #'tpot.builtins.ZeroCount': {
    #},
    
    #'tpot.builtins.OneHotEncoder': {
    #    'minimum_fraction': [0.05, 0.1, 0.15, 0.2, 0.25],
    #    'sparse': [False]
    #},
    
    # Selectors
    SelectFwe: {
        'alpha': np.arange(0, 0.05, 0.001),
        'score_func': {
            f_classif: None
        }
    },
    
    SelectPercentile: {
        'percentile': range(1, 100),
        'score_func': {
            f_classif: None
        }
    },
    
   VarianceThreshold: {
        'threshold': np.arange(0.05, 1.01, 0.05)
    }
#   RFE: {
#    'step': np.arange(0.05, 1.01, 0.05),
#    'estimator': {
#            ExtraTreesClassifier : []
#            }
#   },
#   SelectFromModel: {
#       'threshold': np.arange(0, 1.01, 0.05),
#       'estimator': {
#            ExtraTreesClassifier : []
#            }
#    }
#           RFE: {
#    'step': np.arange(0.05, 1.01, 0.05),
#    'estimator': {
#        ExtraTreesClassifier: {
#            'n_estimators': [100],
#            'criterion': ['gini', 'entropy'],
#            'max_features': np.arange(0.05, 1.01, 0.05)
#        }
#    }
#   },
#   SelectFromModel: {
#       'threshold': np.arange(0, 1.01, 0.05),
#       'estimator': {
#           ExtraTreesClassifier: {
#            'n_estimators': [100],
#               'criterion': ['gini', 'entropy'],
#               'max_features': np.arange(0.05, 1.01, 0.05)
#           }
#       }
#    }
}
   
""" 
RFE: {
    'step': np.arange(0.05, 1.01, 0.05),
    'estimator': {
        'sklearn.ensemble.ExtraTreesClassifier': {
            'n_estimators': [100],
            'criterion': ['gini', 'entropy'],
            'max_features': np.arange(0.05, 1.01, 0.05)
        }
    }
},
SelectFromModel: {
    'threshold': np.arange(0, 1.01, 0.05),
    'estimator': {
        'sklearn.ensemble.ExtraTreesClassifier': {
            'n_estimators': [100],
            'criterion': ['gini', 'entropy'],
            'max_features': np.arange(0.05, 1.01, 0.05)
        }
    }
"""
