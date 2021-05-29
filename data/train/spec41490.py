import numpy as np 

def function(x):

	k6 = 6
	q5 = x
	paths = []
	try:
		if x >= 1:
			q5 = 5*q5
			x = x+5
			paths.append(1)
		else:
			q5 = q5+4
			x = 2*x
			x = 2-0
			paths.append(2)
		if k6 <= 4:
			q5 = q5+0
			paths.append(3)
		else:
			k6 = 8/k6
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		k6 = q5**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))