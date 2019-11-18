# gibbs-sampling-inference
Gibbs Sampling Inference Tool, used to perform inference on unseen corpus based on Collapsed Gibbs Sampling method. (Hopefully) Suitable for every Topic Model Algorithm. [Reference](https://www.coursera.org/lecture/ml-clustering-and-retrieval/a-worked-example-for-lda-deriving-the-resampling-distribution-O35EG)

**Neccesary File**
    * Corpus Wide: Collapsed Gibbs Sampling result of corpus based on Topic Model inference from original document. 
    * Vocabulary: List of all vocabulary from original corpus with its ID.
    * New Document:  Unseen document, its latent topics will be revealed.
    * Number of Topics: Number of topics to be revealed, have to be the same with number of topics on *Corpus Wide* file.
    * Number of Iterations: Number of iterations to run inference.
    * Alpha: Alpha value as smoothing parameter for document-topic distribution.
    * Beta: Beta value as smoothing parameter for word-topic distribution.

**How to use**
	$ python inference_tools.py <corpus_wide_file_path> <vocabulary_file_path> <new_document_file_path> <number_of_topics (int)> <number_of_iterations (int)> <alpha (double)> <beta (double)>

**Output**
    $ Dictionary(Key: Words from new document, Value: Its chosen topic).
    $ List[Topic Distribution of new document]

**Example**
    $ python inference_tools.py corpus-wide.txt vocabulary.txt document.txt 7 1000 0.05 0.15
    $ {u'planned_21': 1, u'information_70': 1, u'growing_25': 1, u'utilization_78': 1, u'strategy_1': 1, u'checking_46': 1, u'allowed_31': 1, u'since_0': 1, u'information_37': 1, u'information_33': 1, u'process_35': 1, u'building_76': 1, u'understand_56': 1, u'discussion_26': 1, u'limited_9': 1, u'information_63': 1, u'linking_69': 1, u'centralized_74': 1, u'culture_29': 1, u'effectively_81': 1, u'information_77': 1, u'managed_39': 1, u'platform_79': 1, u'explained_54': 1, u'management_75': 1, u'reliable_64': 1, u'criterion_57': 1, u'planning_65': 1, u'strengthening_11': 1, u'market_73': 1, u'corporate_12': 1, u'material_24': 1, u'sale_68': 1, u'next_14': 1, u'clear_34': 1, u'even_22': 1, u'manufacturing_67': 1, u'multiple_42': 1, u'management_51': 1, u'centrally_38': 1, u'human_18': 1, u'information_41': 1, u'clearly_53': 1, u'used_80': 1, u'quality_50': 1, u'brought_17': 1, u'use_3': 1, u'standard_48': 1, u'use_7': 1, u'active_27': 1, u'asset_71': 1, u'leader_16': 1, u'necessary_32': 1, u'resource_19': 1, u'everyone_55': 1, u'competitiveness_13': 1, u'generation_15': 1, u'lead_10': 1, u'strategy_52': 1, u'process_45': 1, u'legacy_4': 1, u'share_40': 1, u'corporate_28': 1, u'stored_60': 1, u'development_20': 1, u'system_5': 1, u'secondary_6': 1, u'mature_23': 1, u'checking_47': 1, u'create_44': 1, u'data_58': 1, u'determining_36': 1, u'including_72': 1, u'continue_2': 1, u'department_43': 1, u'information_59': 1, u'failure_30': 1, u'development_66': 1, u'clear_62': 1, u'data_8': 1, u'system_61': 1, u'product_49': 1}
    $ {0: 0.0, 1: 1.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0}
