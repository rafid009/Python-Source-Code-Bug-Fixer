import numpy as np 

def function(x):

	q5 = 9
	p3 = x
	paths = []
	try:
		if x > 6:
			p3 = q5/x
			paths.append(1)
		else:
			p3 = 1+p3
			q5 = 1-q5
			q5 = x+x
			paths.append(2)
		if x > 3:
			p3 = 7-x
			x = q5+x
			paths.append(3)
		else:
			x = x*2
			q5 = q5*3
			q5 = x+q5
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