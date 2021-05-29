import numpy as np 

def function(x):

	j2 = x
	i0 = x
	paths = []
	try:
		if j2 <= 3:
			i0 = 0/i0
			j2 = j2-9
			paths.append(1)
		else:
			i0 = 5*i0
			paths.append(2)
		if x <= 4:
			i0 = i0-4
			x = j2/9
			paths.append(3)
		else:
			x = 4/7
			i0 = 8+i0
			x = 1*2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))