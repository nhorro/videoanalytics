import sys
sys.path.append("../../../src")

from videoanalytics.pipeline import Pipeline
from videoanalytics.pipeline.sources import VideoReader
from videoanalytics.pipeline.sinks import VideoWriter

if __name__ == "__main__":
    
    DATA_PATH = "../../data"

    # Input
    INPUT_VIDEO = DATA_PATH+"/test_video.mp4"
    START_FRAME = 0
    MAX_FRAMES = 10

    # Output
    OUTPUT_VIDEO = DATA_PATH+ "/output.mp4"

    # 1. Create the context
    context = {}

    # 2. Create the pipeline
    pipeline = Pipeline()

    # 3. Add components
    pipeline.add_component( VideoReader( "input",context,
                     video_path=INPUT_VIDEO,
                     start_frame=START_FRAME,
                     max_frames=MAX_FRAMES))

    pipeline.add_component(VideoWriter("writer",context,filename=OUTPUT_VIDEO))

    # 4. Define connections
    pipeline.set_connections([
        ("input", "writer")
    ])

    # 5. Execute
    pipeline.execute()

    # 6. Report
    print(pipeline.get_metrics())

