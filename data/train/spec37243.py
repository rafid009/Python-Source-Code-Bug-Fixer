import numpy as np 

def function(x):

	p7 = 3
	q9 = x
	paths = []
	try:
		if p7 > 9:
			x = 6+1
			x = x*x
			p7 = 2*q9
			paths.append(1)
		else:
			q9 = 9/6
			x = q9/5
			q9 = q9-8
			paths.append(2)
		if p7 > 2:
			p7 = p7+0
			p7 = p7-5
			x = 9*2
			paths.append(3)
		else:
			q9 = q9/q9
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))