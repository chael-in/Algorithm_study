def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(t):
        m, s = map(int, t.split(":"))
        return m * 60 + s
    
    def to_time(sec):
        return f"{sec // 60:02d}:{sec % 60:02d}"
    
    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)
    
    def skip_opening(pos):
        if op_start <= pos <= op_end:
            pos = op_end
        return pos
    
    pos = skip_opening(pos)
    
    for command in commands:
        if command == "prev":
            pos = max(0, pos - 10)
        else:
            pos = min(pos + 10, video_len)
            
        pos = skip_opening(pos)
        
    return to_time(pos)