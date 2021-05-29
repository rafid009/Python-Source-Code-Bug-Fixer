import numpy as np 

def function(x):

	q5 = 7
	r1 = 0
	paths = []
	try:
		if x < 7:
			r1 = 5+r1
			q5 = q5+4
			r1 = x-9
			paths.append(1)
		else:
			q5 = 1/9
			paths.append(2)
		if x > 2:
			q5 = q5*7
			paths.append(3)
		else:
			r1 = q5/q5
			q5 = x+0
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))