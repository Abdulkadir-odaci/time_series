# time_series
We ask you to help us out with the problem of forecasting the daily number of orders. We have the daily number of (simulated) orders for from 2nd May 2020 until 30 June 2022. In addition, we have collected data for the temperature and marketing spend.

We are required to run the model every Monday morning and get predictions for the upcoming 2 weeks. Note that the values in the temperature column are real values, hence are just available for current and past days. On the other hand, marketing spend is a feature we can know in advance, so it is available at prediction time.

Moreover, we are not just interested in the point predictions but also in the uncertainty of the predictions.
Before putting this model into production, we need to assess model performance, so please provide information about the out-of-sample-expected performance.

Remember that your future peers will assess this assignment, so treat it as such: A well-structured piece of work that is ready for review, with clean code that’s easy to follow, including comments/narrative where applicable. The returned report should contain enough discussions to explain your thought process and help us understand your reasoning. 

Once done, expose this model with an API endpoint
that can return forecasts for a specified date interval or return forecasts for a given
forecast horizon (i.e., the number of periods ahead one wishes to obtain predictions).

Your task will be evaluated on the following points
Data Exploration
Choice of model and justification for it
Choice of metrics used to obtain the final model and explanation for it
Ease to understand code and project structure
Hosting of an API Endpoint for your fitted model


