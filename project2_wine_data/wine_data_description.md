This dataset contains various physicochemical properties and quality
ratings for red wine samples. The features (fixed acidity, volatile
acidity, citric acid, etc.) are used to predict the quality of the wine,
which is rated on a scale from 0 to 10. Each column represents a
different aspect of the wine\'s composition or its assessed quality.

**Wine Quality - Red Wine Dataset Description**

1.  **Fixed Acidity (fixed acidity)**

    - **Description:** Fixed acids are non-volatile acids that do not
      evaporate easily.

    - **Units:** grams per liter (g/L)

2.  **Volatile Acidity (volatile acidity)**

    - **Description:** Volatile acids can evaporate and contribute to
      the wine\'s aroma and taste.

    - **Units:** grams per liter (g/L)

3.  **Citric Acid (citric acid)**

    - **Description:** Citric acid is a weak organic acid that adds
      freshness and flavor to the wine.

    - **Units:** grams per liter (g/L)

4.  **Residual Sugar (residual sugar)**

    - **Description:** Residual sugar is the amount of sugar remaining
      after fermentation stops.

    - **Units:** grams per liter (g/L)

5.  **Chlorides (chlorides)**

    - **Description:** Chlorides represent the amount of salt in the
      wine.

    - **Units:** grams per liter (g/L)

6.  **Free Sulfur Dioxide (free sulfur dioxide)**

    - **Description:** Free sulfur dioxide is the amount of SO2 that is
      not bound and is available to act as an antimicrobial and
      antioxidant.

    - **Units:** milligrams per liter (mg/L)

7.  **Total Sulfur Dioxide (total sulfur dioxide)**

    - **Description:** Total sulfur dioxide includes both bound and free
      forms of SO2.

    - **Units:** milligrams per liter (mg/L)

8.  **Density (density)**

    - **Description:** Density is the mass per unit volume of the wine,
      influenced by the amount of sugar and alcohol.

    - **Units:** grams per cubic centimeter (g/cm³)

9.  **pH (pH)**

    - **Description:** pH measures the acidity or alkalinity of the
      wine. Lower pH values indicate higher acidity.

    - **Units:** pH scale (dimensionless)

10. **Sulphates (sulphates)**

    - **Description:** Sulphates are added to wine to prevent spoilage
      and oxidation.

    - **Units:** grams per liter (g/L)

11. **Alcohol (alcohol)**

    - **Description:** The alcohol content of the wine.

    - **Units:** percentage by volume (% vol)

12. **Quality (quality)**

    - **Description:** The quality score of the wine, typically based on
      sensory data (taste, aroma, etc.).

    - **Units:** score (integer scale from 0 to 10)

**Questions:**

1.  **What is the most frequently occurring wine quality? What is the
    highest number in and the lowest number in the quantity column?**

2.  **How is \`fixed acidity\` correlated to the quality of the wine?
    How does the alcohol content affect the quality? How is the \`free
    Sulphur dioxide\` content correlated to the quality of the wine?**

3.  **What is the average \`residual sugar\` for the best quality wine
    and the lowest quality wine in the dataset?**

4.  **Does \`volatile acidity\` has an effect over the quality of the
    wine samples in the dataset?**

5.  **Train a Decision Tree model and Random Forest Model separately to
    predict the Quality of the given samples of wine. Compare the
    Accuracy scores for both models.**
