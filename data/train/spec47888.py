import numpy as np 

def function(x):

	q6 = x
	f1 = x
	paths = []
	try:
		if f1 > 7:
			q6 = 5+x
			f1 = 9*x
			f1 = 1-f1
			paths.append(1)
		else:
			x = x*q6
			q6 = 4*0
			f1 = 3/6
			paths.append(2)
		if f1 <= 1:
			x = x-8
			q6 = 6+q6
			paths.append(3)
		else:
			f1 = 2-f1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))