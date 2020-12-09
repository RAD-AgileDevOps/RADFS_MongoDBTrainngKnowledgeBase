/*
Developer: Roger De Four
Date: 2020-11-17
Description: Data Analysis to review my MongoDB querying skills

*/


// The following query searches for date 16th Nov 2020
db.col_ecdcCOVID19_20201117.find({"dateRep": {$eq:"16/11/2020"}})