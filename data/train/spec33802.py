import numpy as np 

def function(x):

	m9 = 1
	q9 = 8
	paths = []
	try:
		if m9 <= 5:
			q9 = x-q9
			paths.append(1)
		else:
			x = q9+x
			paths.append(2)
		if q9 < 4:
			x = x*2
			paths.append(3)
		else:
			q9 = 9+q9
			q9 = m9/m9
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