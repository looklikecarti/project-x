#3 It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.xThis function should return a dictionary in the form of (use the correct numbers): {"male":0.2,"female":0.4} Note: To aid in verification, the chickenpox_by_sex()['female'] value the autograder is looking for starts with the digits 0.0077.import pandas as pd
data = {
    'sex': ['male', 'male', 'female', 'female', 'male', 'female', 'male', 'female'],
    'had_chickenpox': [1, 0, 1, 1, 1, 0, 0, 1],
    'vaccinated': [1, 1, 1, 1, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
def chickenpox_by_sex():
    vaccinated = df[(df['vaccinated'] == 1) & (df['had_chickenpox'] == 1)]
    vaccinated_no = df[(df['vaccinated'] == 1) & (df['had_chickenpox'] == 0)]
    ratio_male = vaccinated[vaccinated['sex'] == 'male'].shape[0] / \
                 vaccinated_no[vaccinated_no['sex'] == 'male'].shape[0]
    ratio_female = vaccinated[vaccinated['sex'] == 'female'].shape[0] / \
                   vaccinated_no[vaccinated_no['sex'] == 'female'].shape[0]
    return {"male": ratio_male, "female": ratio_female}
result = chickenpox_by_sex()
print(result)


#4 A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella). Some notes on interpreting the answer. The had_chickenpox_column is either 1 (for yes) or 2 (for no), and the num_chickenpox_vaccine_column is the number of doses a child has been given of the varicella vaccine. A positive correlation (e.g., corr > 0) means that an increase in had_chickenpox_column (which means more no’s) would also increase the values of num_chickenpox_vaccine_column (which means more doses of vaccine). If there is a negative correlation (e.g., corr < 0), it indicates that having had chickenpox is related to an increase in the number of vaccine doses. Also, pval is the probability that we observe a correlation between had_chickenpox_column and num_chickenpox_vaccine_column which is greater than or equal to a particular value occurred by chance. A small pval means that the observed correlation is highly unlikely to occur by chance. In this case, pval should be very small (will end in e-18 indicating a very small number). [1] This isn’t really the full picture, since we are not looking at when the dose was given. It’s possible that children had chickenpox and then their parents went to get them the vaccine. Does this dataset have the data we would need to investigate the timing of the dose? def corr_chickenpox(): import scipy.stats as stats import numpy as np import pandas as pd # this is just an example dataframe df=pd.DataFrame({"had_chickenpox_column":np.random.randint(1,3,size=(100)), "num_chickenpox_vaccine_column":np.random.randint(0,6,size=(100))}  # here is some stub code to actually run the correlation corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"]) # just return the correlation #return corr # YOUR CODE HERE raise NotImplementedError()
def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    df = pd.DataFrame({
        "had_chickenpox_column": np.random.randint(1, 3, size=(100)),
        "num_chickenpox_vaccine_column": np.random.randint(0, 6, size=(100))
    })
    corr, pval = stats.pearsonr(df["had_chickenpox_column"], df["num_chickenpox_vaccine_column"])
    return corr, pval
correlation, p_value = corr_chickenpox()
print("Correlation:", correlation)
print("P-value:", p_value)