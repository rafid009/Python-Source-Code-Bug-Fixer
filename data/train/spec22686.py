import numpy as np 

def function(x):

	q5 = x
	r6 = 6
	paths = []
	try:
		if q5 >= 0:
			x = 4+x
			paths.append(1)
		else:
			r6 = r6*r6
			paths.append(2)
		if r6 > 8:
			x = q5*9
			x = q5-x
			r6 = 8+r6
			paths.append(3)
		else:
			x = 1-7
			x = 4/8
			x = 0*7
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))