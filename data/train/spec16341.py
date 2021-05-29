import numpy as np 

def function(x):

	f1 = x
	q5 = 2
	paths = []
	try:
		if q5 > 4:
			x = 2-x
			paths.append(1)
		else:
			f1 = f1*3
			q5 = x*7
			f1 = f1+9
			paths.append(2)
		if q5 <= 6:
			f1 = x*0
			paths.append(3)
		else:
			q5 = q5/1
			x = 2+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))