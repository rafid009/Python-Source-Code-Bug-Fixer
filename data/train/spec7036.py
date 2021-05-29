import numpy as np 

def function(x):

	b9 = x
	j2 = x
	paths = []
	try:
		if j2 < 3:
			j2 = j2-2
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if j2 <= 5:
			b9 = 0-7
			j2 = 9-j2
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		j2 = b9**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))