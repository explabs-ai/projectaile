{
	"MODEL": {
		"MODEL_NAME": "scfegan",
		"MODEL_DESCRIPTION": "SC-FEGAN: Face Editing Generative Adversarial Network with User’s Sketch and Color",
		"MODEL_TYPE": "gan",
		"PROBLEM_TYPE": "inpainting",
		"MODEL_PARAMS": {
			"INPUT_SHAPE": [224, 224, 3],
			"KERNEL_SIZE": [3, 3],
			"STRIDES": [2, 2]
		}
	},
	"DATASET": {
		"INTERFACE_TYPE": "directory",
		"INTERFACE_PATH": "",
		"DATA_PATH": "_path_to_celeba_dset_",
		"DIRECTORIES": "",
		"TRAIN_TEST_SPLIT": true,
		"INPUT_TYPE": "image",
		"TARGET_PATH": ""
	},
	"HYPERPARAMETERS": {
		"TRAINING_BATCH_SIZE": 8,
		"NUM_EPOCHS": 100,
		"STEPS_PER_EPOCH": 0,
		"LEARNING_RATE": 1e-3,
		"MONITOR_METRIC": "val_loss",
		"SAVE_WEIGHTS": true,
		"EARLY_STOP_EPOCHS": 2,
		"DROPOUT_RATIO": 0.3,
		"LR_DECAY_ALPHA": 0.4
	},
	"CONFIG_INFO": {
		"LOG_DIR": "logs",
		"MODEL_IMAGE_PATH": "model_images",
		"CHECKPOINTS_PATH": "checkpoints"
	}
}