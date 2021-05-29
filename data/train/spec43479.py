import numpy as np 

def function(x):

	j9 = 4
	q5 = x
	paths = []
	try:
		if j9 > 0:
			q5 = 0+j9
			j9 = j9-8
			x = q5-8
			paths.append(1)
		else:
			j9 = 8/7
			q5 = 2*q5
			q5 = 2+q5
			paths.append(2)
		if q5 > 0:
			q5 = 5/q5
			x = q5/x
			x = 4+x
			paths.append(3)
		else:
			x = 2-x
			j9 = j9/5
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))