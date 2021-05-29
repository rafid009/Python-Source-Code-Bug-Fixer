import numpy as np 

def function(x):

	q5 = x
	j5 = x
	paths = []
	try:
		if j5 >= 8:
			q5 = 5/q5
			x = 2-0
			x = j5*2
			paths.append(1)
		else:
			x = q5-5
			j5 = j5-j5
			paths.append(2)
		if q5 <= 1:
			j5 = 1-x
			j5 = 4+1
			j5 = j5-8
			paths.append(3)
		else:
			q5 = x/q5
			x = j5-j5
			j5 = j5-2
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