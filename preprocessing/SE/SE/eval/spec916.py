import numpy as np 

def function(x):

	q5 = 1
	p2 = x
	paths = []
	try:
		if x >= 6:
			p2 = p2-7
			paths.append(1)
		else:
			p2 = q5-0
			paths.append(2)
		if q5 <= 8:
			q5 = q5-6
			p2 = 3-p2
			paths.append(3)
		else:
			x = x/6
			q5 = p2+7
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