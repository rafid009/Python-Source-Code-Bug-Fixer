import numpy as np 

def function(x):

	i1 = x
	m5 = x
	paths = []
	try:
		if i1 < 2:
			x = x-8
			paths.append(1)
		else:
			i1 = 6-i1
			x = x*1
			x = 4+x
			paths.append(2)
		if x < 4:
			m5 = m5+m5
			x = 6-3
			x = 6-x
			paths.append(3)
		else:
			i1 = i1+9
			x = m5/3
			i1 = x-i1
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