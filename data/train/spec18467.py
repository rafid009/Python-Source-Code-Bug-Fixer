import numpy as np 

def function(x):

	m8 = 5
	i1 = x
	paths = []
	try:
		if i1 <= 4:
			i1 = i1/9
			x = 6-0
			paths.append(1)
		else:
			x = m8+x
			paths.append(2)
		if x < 2:
			i1 = m8/m8
			i1 = i1+7
			i1 = 8/i1
			paths.append(3)
		else:
			x = x+x
			m8 = m8+x
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))