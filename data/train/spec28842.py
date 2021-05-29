import numpy as np 

def function(x):

	q5 = 9
	n8 = x
	paths = []
	try:
		if x >= 2:
			q5 = q5/n8
			paths.append(1)
		else:
			q5 = q5-q5
			n8 = n8+1
			x = x/5
			paths.append(2)
		if x >= 1:
			n8 = 1*n8
			paths.append(3)
		else:
			q5 = n8+x
			n8 = 1+q5
			n8 = q5-n8
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		n8 = q5**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))