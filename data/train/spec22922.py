import numpy as np 

def function(x):

	q5 = x
	v6 = 3
	paths = []
	try:
		if x > 6:
			x = 1+5
			v6 = 1/8
			q5 = v6/3
			paths.append(1)
		else:
			v6 = 4+q5
			x = x/5
			paths.append(2)
		if q5 <= 3:
			x = 6+2
			paths.append(3)
		else:
			q5 = q5/x
			x = x+7
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		v6 = q5**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))