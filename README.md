# data-fusion-contest
Решение первой задачи контеста https://boosters.pro/championship/data_fusion/overview  
Скор на публичном лидерборде 0.8562009 (19 место из 265).  
Основная идея решения:
1. Дообучаем distilbert на задаче masked language modeling. 
2. Модель из п.1. дообучаем на задаче многоклассовой классификации. Используем только размеченные данные (дообученая модель расположена в distilbert_uncased_for_pseudolab/).
3. Используем агломеративную кластеризацию для псевдо разметки (подробнее про метод можно прочитать здесь https://www.aclweb.org/anthology/2020.coling-main.438.pdf).  
Псевдо размеченные данные расположены в data/pseudo.csv.
5. Используем SVM + TFIDF на размеченных и псевдо размеченных данных.

Notebooks:
1. data_fusion_task1_BERTML.ipynb - дообучение distilbert на задаче masked language modeling.
2. DISTILBERT_with_pseudo.ipynb - дообучение distilbert из п.2 на задаче классификации item_name из чеков и псевдоразметка данных.
3. task1_data_fusion.ipynb - SVM + TFIDF классификация item_name из чеков.
