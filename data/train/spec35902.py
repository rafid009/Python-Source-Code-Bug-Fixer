import numpy as np 

def function(x):

	f5 = 2
	q5 = 5
	paths = []
	try:
		if q5 <= 5:
			f5 = 8*x
			q5 = 8/q5
			paths.append(1)
		else:
			f5 = x-1
			f5 = 4*f5
			q5 = x+q5
			paths.append(2)
		if q5 >= 8:
			f5 = f5+0
			f5 = 2+1
			paths.append(3)
		else:
			x = f5+x
			x = x/9
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		q5 = f5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))