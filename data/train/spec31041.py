import numpy as np 

def function(x):

	q5 = x
	n9 = 9
	paths = []
	try:
		if x < 4:
			n9 = n9-6
			paths.append(1)
		else:
			n9 = n9/9
			paths.append(2)
		if x < 7:
			n9 = n9+3
			q5 = n9-8
			x = x-9
			paths.append(3)
		else:
			q5 = q5-n9
			q5 = 1+q5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		n9 = q5**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))