import numpy as np 

def function(x):

	i9 = x
	m7 = 8
	x = x
	paths = []
	try:
		if i9 >= 4:
			x = x*1
			i9 = 1-i9
			m7 = 0+x
			paths.append(1)
		else:
			i9 = 2*i9
			i9 = x*1
			m7 = m7+m7
			paths.append(2)
		if x <= 3:
			x = x*0
			i9 = i9/i9
			i9 = 5*i9
			paths.append(3)
		else:
			m7 = m7*i9
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))