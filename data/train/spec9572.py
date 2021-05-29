import numpy as np 

def function(x):

	m7 = 0
	v8 = 9
	paths = []
	try:
		if v8 >= 4:
			v8 = x-x
			paths.append(1)
		else:
			x = 0*m7
			m7 = m7*6
			paths.append(2)
		if x < 1:
			v8 = v8*2
			m7 = m7*6
			paths.append(3)
		else:
			v8 = v8-1
			m7 = 9-m7
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		m7 = v8**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))