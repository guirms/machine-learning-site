export interface PredictResult {
    best_accuracy: number;
    best_params: BestParams;
    classification_report: ClassificationReport;
    model: string;
}

interface BestParams {
    C?: number;
    gamma?: number;
    kernel?: string;
    metric?: string;
    n_neighbors?: number;
    weights?: string;
    criterion?: string;
    min_samples_leaf?: number;
    min_samples_split?: number;
    splitter?: string;
}

interface F1Score {
    accuracy?: number;
    b: number;
    m: number;
    macro_avg: number;
    weighted_avg: number;
}

interface ClassificationReport {
    f1_score: F1Score;
    precision: F1Score;
    recall: F1Score;
    support: F1Score; 
}


