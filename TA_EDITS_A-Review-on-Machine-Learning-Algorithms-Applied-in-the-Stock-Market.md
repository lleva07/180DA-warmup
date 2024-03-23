<span style="color:red">Sunay Comments</span>
<span style="color:red">[</span>Text to consider deleting<span style="color:red">[</span>

## I. Introduction
The stock market has always been highly data-driven in order to make substantial profits. Exchanges such as NASDAQ possess historical records on stock movements of various companies ever since its foundation during the 1970s. <span style="color:red">[</span>As such,<span style="color:red">]</span> this information was <span style="color:red">[</span>highly<span style="color:red">]</span> valuable for traders <span style="color:red">[</span>employing trading strategies<span style="color:red">]</span> reliant on charting and the use of technical indicators.

<span style="color:red">First sentence wording is confusing/imprecise.</span>

In this modern age, market participants are able to execute near-instantaneous trades through online brokerage accounts. The outcomes of various trades <span style="color:red">[</span>may very well be<span style="color:red">]</span> <span style="color:red">are</span> dictated by the participant’s ability to effectively analyze fluctuating data and execute trades in a matter of seconds. <span style="color:red">[</span>Therefore<span style="color:red">]</span>, the development of quick, robust, and technically advanced approaches to stock market trading are needed. As such, the application of machine learning algorithms is exactly what is needed to execute high frequency trades.

This article aims to evaluate the application of various machine learning algorithms in the stock market such as regression-based models, time series forecasting models, and deep learning models.

<span style="color:red">The intro covers all the necessary points. Focus on concise language, trimming words and also combining repeatative language and phrases. For example: "Machine learning algorithms such as ... are essential for executing profitable high frequency trades" condenses the last 3 sentences down. </span>

## II. Machine Learning Algorithms for Stock Market Prediction

# Linear Regression Model
The “Linear Regression” (<span style="color:red">No quotes or capitalization needed</span>) is one of the simplest machine learning algorithms used in the stock market. The fundamental points are that this algorithm uses a regression equation to establish a linear relationship between dependent and independent variables to visualize general trends. Depending on the type of analysis being performed, the introduction of multiple independent variables(e.g. Trading volume, market capitalization) to see a more generalized effect towards the dependent variable(e.g stock price). Despite this, the downside of this model is that it may be harder to model complex patterns that may arise from non-linear trends within the dataset.

# Autoregressive Integrated Moving Average Model (ARIMA)
The ARIMA model is a popular time series forecasting technique. This model is built on 3 key components: Autoregression which models how current values are dependent on past values, Integrated converts the time series data to a stationary format to better understand underlying trends, Moving Average which eliminates noise from outliers to better visualize a stock trend. Overall, the ARIMA model is strongly suited for short term trades based solely off of historical market data. Consequently, it is vulnerable to market sentiment that may arise from news such as trade embargoes, resource shortages, etc.

<span style="color:red">Get a little more into the technical detaiuls in these sections, and not just what is happening at a high level. Use plenty of visuals and examples (possibly a running example through all sections would help).</span>

# Deep Q-Networks (DQN)
The DQN model is a combination of both deep learning and reinforcement learning. The general idea behind the DQN model is that it uses an agent to continuously interact within a specified environment. Furthermore, it uses the concepts of states to analyze its relative situation within the environment and a Q-function to approximate the most ideal action given a certain state. Based on this action, the agent adopts a reinforcement learning approach to either reward or penalize the model based on the action adopted. <span style="color:red">Precise language: the "agent" doesn't adopt the RL approach</span> To further optimize a DQN, raw data may be preprocessed such that the agent is able to adopt various technical indicators and market sentiment. As such, the DQN is highly suitable for short and long term analysis of stocks considering that it can learn various trading strategies faster. Despite its highly robust nature, the development of such models are computationally expensive and time consuming to implement. 

# Long Short Term Memory (LSTM) Model
The “Long Short Term Memory” falls under the realm of both time forecasting and deep learning. LSTMs are built off of recurrent neural network(RNN) architecture. However, what differentiates this model from RNNs is the presence of memory cells that are ideal for learning long term dependencies in market data. Consequently, LSTMs are computationally expensive arising from the fact that they require large datasets to properly learn complex trends in market data. Moreover, this model is easily overfitted depending on the architecture complexity.

## III. Conclusion
The review of the various approaches has explored the application of machine learning algorithms in the stock market. From the simplicity of linear regression to the complex and robust nature of deep q-networks, each algorithm has offered their own unique strengths and limitations towards market analysis. 
In order to capitalize on these strengths, it is recommended that further investigation be done on the implementation of hybrid or combination models to address the weaknesses of certain models. Aside from this, research on architecture optimization arising from this hybrid model must be done in order to effectively implement these new approaches to market analysis.

<span style="color:red">This isn't a research paper so you don't need a "further work" recommendations section. Your article will benefit a lot from a combination of examples and visuals. The examples will also help tie up the conclusion where you can summarize the various methods and trade-offs with more specifics. </span>

# References:
https://www.investopedia.com/terms/a/autoregressive-integrated-moving-average-arima.asp
https://www.tensorflow.org/agents/tutorials/0_intro_rl
https://www.investopedia.com/terms/m/movingaverage.asp#:~:text=The%20Bottom%20Line-,A%20moving%20average%20(MA)%20is%20a%20stock%20indicator%20commonly%20used,moving%20average%20indicates%20a%20downtrend.
https://medium.com/@anishnama20/understanding-lstm-architecture-pros-and-cons-and-implementation-3e0cca194094
