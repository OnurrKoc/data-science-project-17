import numpy as np
import matplotlib.pyplot as plt
def five_number_summary(data: list) -> dict:
    return {
        "min": min(data),
        "Q1": float(np.percentile(data, 25)),
        "median": float(np.median(data)),
        "Q3": float(np.percentile(data, 75)),
        "max": max(data)
    }
    """
    Min, Q1, Median, Q3, Max değerlerini içeren sözlük döndür.
    Output örneği: {'min': ..., 'Q1': ..., 'median': ..., 'Q3': ..., 'max': ...}
    """

def detect_outliers(data: list) -> list:
    q1 = float(np.percentile(data, 25))
    q3 = float(np.percentile(data, 75))
    iqr = q3 - q1
    alt = q1 - 1.5 * iqr
    ust = q3 + 1.5 * iqr
    return [x for x in data if x < alt or x > ust]
    """
    IQR metoduyla aykırı değerleri tespit et.
    Output: [list of outliers]
    """

def draw_boxplot(data: list) -> None:
    plt.boxplot(data)
    plt.title("Boxplot")
    plt.show()
    """
    Verinin boxplot'unu çiz.
    Output: matplotlib görseli
    """

def draw_histogram(data: list, title: str = "Histogram") -> None:
    plt.hist(data, bins=10)
    plt.title(title)
    plt.show()
    """
    Histogramı çiz.
    """
from scipy.stats import skew
#Input: [1, 2, 3, 4, 100]
#Output: skewness değeri, > 0 ise sağa çarpık
def calculate_skewness(data: list) -> float:
    return float(skew(data))
    """
    Veri setinin skewness (çarpıklık) değerini hesapla.
    """

#Input: [1, 2, 3, 4, 100]
#skewness değerini hesaplamalısın. bu değere göre 'left', 'right' veya 'symmetric' değerini döndür
def is_skewed(data: list) -> str:
    s = calculate_skewness(data)
    if s > 0.5:
        return "right"
    elif s < -0.5:
        return "left"
    else:
        return "symmetric"
    """
    Skewness değerine göre 'left', 'right' veya 'symmetric' döndür.
    """

def calculate_covariance(x: list, y: list) -> float:
    return float(np.cov(x, y, ddof=1)[0][1])
    """
    İki veri seti arasındaki kovaryansı hesapla.
    """

def calculate_correlation(x: list, y: list) -> float:
    return float(np.corrcoef(x, y)[0][1])
    """
    Pearson correlation coefficient hesapla.
    """

def is_positive_correlation(x: list, y: list) -> bool:
    return calculate_correlation(x, y) > 0
    """
    Korelasyon pozitif mi kontrol et.
    """

def compare_variables(x: list, y: list) -> dict:
    return {
        "covariance": calculate_covariance(x, y),
        "correlation": calculate_correlation(x, y)
    }
    """
    Hem kovaryans hem de korelasyonu döndür.
    Output: {'covariance': ..., 'correlation': ...}
    """