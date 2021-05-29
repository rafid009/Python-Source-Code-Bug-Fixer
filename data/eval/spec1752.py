import numpy as np 

def function(x):

	j2 = 4
	i7 = x
	paths = []
	try:
		if j2 <= 6:
			i7 = i7-2
			j2 = j2*4
			j2 = x-j2
			paths.append(1)
		else:
			j2 = j2*0
			paths.append(2)
		if i7 >= 8:
			i7 = i7-1
			paths.append(3)
		else:
			i7 = i7/5
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