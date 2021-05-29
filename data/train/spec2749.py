import numpy as np 

def function(x):

	q5 = 3
	r8 = x
	paths = []
	try:
		if r8 < 2:
			q5 = q5+3
			paths.append(1)
		else:
			q5 = q5/q5
			q5 = 6+7
			q5 = q5*7
			paths.append(2)
		if r8 < 8:
			r8 = 4+r8
			paths.append(3)
		else:
			r8 = r8+1
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))