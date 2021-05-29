import numpy as np 

def function(x):

	q5 = x
	t5 = x
	paths = []
	try:
		if x >= 8:
			x = t5*q5
			q5 = q5*3
			paths.append(1)
		else:
			q5 = 8+3
			q5 = 3*q5
			q5 = q5-x
			paths.append(2)
		if t5 < 6:
			q5 = 9+1
			t5 = x*8
			paths.append(3)
		else:
			q5 = q5/7
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		q5 = t5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))